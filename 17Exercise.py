"""
settings.py
-----------
All constants and tunable numbers for the game live here.
Keeping them in one place makes the game easy to balance and read.
"""

# ----------------------------------------------------------------------
# Screen / timing
# ----------------------------------------------------------------------
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FPS = 60
GAME_TITLE = "City Bus Driver"

# ----------------------------------------------------------------------
# Colors (R, G, B)
# ----------------------------------------------------------------------
COLOR_SKY_TOP = (135, 190, 235)
COLOR_SKY_BOTTOM = (200, 225, 245)
COLOR_GRASS = (72, 130, 70)
COLOR_SIDEWALK = (150, 150, 150)
COLOR_ROAD = (55, 55, 60)
COLOR_ROAD_EDGE = (230, 230, 230)
COLOR_LANE_LINE = (235, 210, 60)
COLOR_LANE_DASH = (240, 240, 240)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (20, 20, 20)
COLOR_RED = (210, 60, 55)
COLOR_DARK_RED = (150, 30, 30)
COLOR_GREEN = (60, 180, 90)
COLOR_DARK_GREEN = (35, 110, 55)
COLOR_YELLOW = (245, 200, 40)
COLOR_ORANGE = (235, 140, 40)
COLOR_BLUE = (60, 120, 210)
COLOR_GRAY = (120, 120, 125)
COLOR_DARK_GRAY = (70, 70, 75)
COLOR_LIGHT_GRAY = (200, 200, 205)
COLOR_BROWN = (110, 75, 45)
COLOR_BUS_BODY = (235, 195, 30)
COLOR_BUS_TRIM = (40, 90, 160)
COLOR_GLASS = (170, 215, 235)

UI_PANEL_BG = (25, 30, 40, 190)  # RGBA, used on a per-surface alpha layer
UI_ACCENT = (245, 200, 40)

# ----------------------------------------------------------------------
# Road layout
# ----------------------------------------------------------------------
ROAD_LEFT = 250
ROAD_RIGHT = 650
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT
SIDEWALK_WIDTH = 45
LANE_COUNT = 4  # 2 lanes each direction
LANE_WIDTH = ROAD_WIDTH // LANE_COUNT

# x-centers of each lane, left to right
LANE_CENTERS = [ROAD_LEFT + LANE_WIDTH * (i + 0.5) for i in range(LANE_COUNT)]
# Lanes 0,1 -> oncoming traffic (moving toward the player / up the screen)
# Lanes 2,3 -> same-direction traffic (moving with the player / down the screen)
ONCOMING_LANES = LANE_CENTERS[0:2]
SAME_DIR_LANES = LANE_CENTERS[2:4]

BUS_STOP_X = ROAD_RIGHT + SIDEWALK_WIDTH / 2  # bus stops sit on the right sidewalk

# ----------------------------------------------------------------------
# Bus
# ----------------------------------------------------------------------
BUS_WIDTH = 70
BUS_HEIGHT = 110
BUS_SCREEN_Y = SCREEN_HEIGHT - 190  # fixed vertical position of the bus on screen

BUS_MAX_SPEED = 130.0        # km/h
BUS_MAX_REVERSE_SPEED = -25.0
BUS_ACCELERATION = 34.0      # km/h per second
BUS_BRAKE_POWER = 70.0       # km/h per second
BUS_FRICTION = 18.0          # natural slow-down when no input, km/h per second
BUS_STEER_SPEED = 260.0      # pixels per second, sideways movement
BUS_MIN_STEER_SPEED_KMH = 4.0  # bus must be moving at least this fast to steer

# Conversion from bus speed (km/h) to world scroll speed (pixels / second)
SPEED_TO_SCROLL = 2.6

PASSENGER_CAPACITY = 8

# ----------------------------------------------------------------------
# Fuel / health
# ----------------------------------------------------------------------
FUEL_MAX = 100.0
FUEL_DRAIN_IDLE = 0.35          # per second, always draining a little
FUEL_DRAIN_PER_SPEED = 0.02     # extra drain proportional to speed
FUEL_REFILL_AMOUNT = 55.0

HEALTH_MAX = 100.0
DAMAGE_TRAFFIC_COLLISION = 22.0
DAMAGE_CURB_HIT = 8.0
COLLISION_INVULNERABLE_TIME = 1.0   # seconds of invulnerability after a hit
COLLISION_SPEED_PENALTY = 35.0      # km/h suddenly lost on collision

# ----------------------------------------------------------------------
# Traffic
# ----------------------------------------------------------------------
TRAFFIC_SPAWN_INTERVAL_MIN = 0.9   # seconds
TRAFFIC_SPAWN_INTERVAL_MAX = 2.0
TRAFFIC_MAX_ON_SCREEN = 9
TRAFFIC_MIN_SPEED = 25.0
TRAFFIC_MAX_SPEED = 70.0
VEHICLE_WIDTH = 62
VEHICLE_HEIGHT = 96

# ----------------------------------------------------------------------
# Bus stops
# ----------------------------------------------------------------------
STOP_SPAWN_INTERVAL_MIN = 6.0
STOP_SPAWN_INTERVAL_MAX = 10.0
STOP_INTERACT_SPEED_THRESHOLD = 6.0   # km/h, must be nearly stopped
STOP_WIDTH = 40
STOP_HEIGHT = 70
EVERY_NTH_STOP_IS_DESTINATION = 3
PASSENGERS_MIN_WAITING = 1
PASSENGERS_MAX_WAITING = 4

SCORE_PER_PICKUP = 15
SCORE_PER_DROPOFF = 40
SCORE_PER_METER = 0.5

# ----------------------------------------------------------------------
# Fuel stations
# ----------------------------------------------------------------------
FUEL_STATION_SPAWN_INTERVAL_MIN = 16.0
FUEL_STATION_SPAWN_INTERVAL_MAX = 26.0
FUEL_STATION_WIDTH = 46
FUEL_STATION_HEIGHT = 60

# ----------------------------------------------------------------------
# Environment decoration (buildings / trees)
# ----------------------------------------------------------------------
BUILDING_MIN_WIDTH = 70
BUILDING_MAX_WIDTH = 130
BUILDING_MIN_HEIGHT = 120
BUILDING_MAX_HEIGHT = 260
TREE_SPACING_MIN = 90
TREE_SPACING_MAX = 170

# ----------------------------------------------------------------------
# Difficulty scaling
# ----------------------------------------------------------------------
DIFFICULTY_RAMP_METERS = 4000.0  # distance over which difficulty ramps up fully