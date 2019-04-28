public static int GRID_WIDTH = 10;
public static PVector UP =  new PVector(0, -1);
public static PVector DOWN = new PVector(0, 1);
public static PVector LEFT = new PVector(-1, 0);
public static PVector RIGHT = new PVector(1, 0);

static class Color {
  public static int WALL = #FF4444;
  public static int BACKGROUND = 245;
  public static int TEXT = #22BBFF;
  public static int LOST_TEXT = #EE4444;
  public static int SERPENT = #88ED77;
  public static int FOOD = #33FD22;
  public static int SERPENT_TEXT = #EE2277;
}

float pixelCoord(float gridCoord) {
  return gridCoord * GRID_WIDTH;
}

PVector pixelCoord(PVector gridCoord) {
  return gridCoord.copy().mult(GRID_WIDTH);
}

int gridCoord(int drawCoord) {
  return drawCoord / GRID_WIDTH;
}
