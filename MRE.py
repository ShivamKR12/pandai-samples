from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.task import Task

from panda3d.ai import *
import EggPrimitiveCreation
from NavMeshGenerator import NavMeshGenerator


class Game(ShowBase):
    def __init__(self):
        super().__init__()

        # --- Scene ---
        # self.disableMouse()
        self.setup_camera()
        self.setup_lighting()

        # --- World ---
        self.load_level()
        self.setup_ai_world()
        self.build_navmesh()

        # --- NPC ---
        self.npc = AINPC(
            name="npc_1",
            model="models/ralph",
            start_pos=Vec3(20, 20, 0),
            ai_world=self.ai_world
        )

        # --- Target marker ---
        self.target = self.create_target(Vec3(120, 120, 0))

        # --- Input ---
        self.accept("enter", self.move_npc)

        # --- Update ---
        self.taskMgr.add(self.update_ai, "update_ai")

    # --------------------------------------------------
    # Scene setup
    # --------------------------------------------------

    def setup_camera(self):
        self.camera.setPos(100, 100, 200)
        self.camera.lookAt(100, 100, 0)

    def setup_lighting(self):
        light = DirectionalLight("sun")
        light.setColor(Vec4(1, 1, 1, 1))
        light_np = render.attachNewNode(light)
        light_np.setHpr(45, -60, 0)
        render.setLight(light_np)

    def load_level(self):
        self.environ = loader.loadModel("models/arena_1.bam")
        self.environ.reparentTo(render)
        self.environ.setScale(1)
        self.environ.setPos(0, 0, 0)

    # --------------------------------------------------
    # AI setup
    # --------------------------------------------------

    def setup_ai_world(self):
        self.ai_world = AIWorld(render)

    def build_navmesh(self):
        # Generate grid
        full = EggPrimitiveCreation.makeSquaresEVPXZ(
            gridX=30, gridY=30, scale=10, evpName="Full"
        )
        coll = EggPrimitiveCreation.makeSquaresEVPXZ(
            gridX=30, gridY=30, scale=10, evpName="Coll"
        )

        full.writeEgg(Filename("nav_full.egg"))
        coll.writeEgg(Filename("nav_coll.egg"))

        # Convert to PandAI CSV
        NavMeshGenerator("nav_full.egg", "nav_coll.egg")

    # --------------------------------------------------
    # Gameplay
    # --------------------------------------------------

    def create_target(self, pos):
        marker = loader.loadModel("models/1m_sphere_black_marble.bam")
        marker.setScale(3)
        marker.setColor(1, 0, 0)
        marker.setPos(pos)
        marker.reparentTo(render)
        return marker

    def move_npc(self):
        self.npc.move_to(self.target)

    def update_ai(self, task):
        self.ai_world.update()
        return Task.cont


# ======================================================
# Reusable AI NPC class
# ======================================================

class AINPC:
    def __init__(self, name, model, start_pos, ai_world):
        self.actor = Actor(
            model,
            {"walk": f"{model}-walk", "run": f"{model}-run"}
        )
        self.actor.reparentTo(render)
        self.actor.setScale(2)
        self.actor.setPos(start_pos)

        self.ai_char = AICharacter(
            name,
            self.actor,
            mass=60,
            movt_force=0.05,
            max_force=20
        )

        ai_world.addAiChar(self.ai_char)
        self.behaviors = self.ai_char.getAiBehaviors()
        self.behaviors.initPathFind("navmesh.csv")

    def move_to(self, target):
        self.behaviors.pathFindTo(target, "path")
        self.actor.loop("run")


# ------------------------------------------------------
# Run
# ------------------------------------------------------

Game()
base.run()
