class Stats {
  boolean gameEnd = false;
  int points = 0;

  void gameEnd() {
    gameEnd = true;
  }

  void nextStep() {
    points++;
  }

  void draw() {
    fill(Color.TEXT);
    textSize(8);
    text(floor(frameRate), width - 30, 10);

    textSize(14);
    text(points, width / 2, 20);

    if (gameEnd) {
      fill(20, 150);
      rect(0, 0, width, height);
      fill(Color.LOST_TEXT);
      textSize(28);
      text("Game lost.", width / 2 - 60, height / 2);
      strokeWeight(1);
    }
  }
}

class Walls {
  private Wall[] walls;

  Walls() {
    walls = new Wall[5];
    int maxGridX = gridCoord(width);
    int maxGridY = gridCoord(height);
    walls[0] = new Wall(0, 0, maxGridX, 3);
    walls[1] = new Wall(0, maxGridY - 1, maxGridX, 1);
    walls[2] = new Wall(0, 0, 1, maxGridY);
    walls[3] = new Wall(maxGridX - 1, 0, 1, maxGridY);
    walls[4] = new Wall(12, 10, 20, 4);
  }

  boolean isPointInWalls(PVector point) {
    for (Wall w : walls) {
      if (w.isPointInWall(point)) {
        return true;
      }
    }
    return false;
  }

  void draw() {
    for (Wall wall : walls) {
      wall.draw();
    }
  }
}

class Wall {
  PVector gridA, gridB, drawPos, drawSize;

  Wall(int x, int y, int w, int h) {
    gridA = new PVector(x, y);
    gridB = gridA.copy().add(w, h);
    drawPos = new PVector(pixelCoord(x), pixelCoord(y));
    drawSize = new PVector(pixelCoord(w), pixelCoord(h));
  }

  void draw() {
    fill(Color.WALL);
    rect(drawPos.x, drawPos.y, drawSize.x, drawSize.y);
  }

  boolean isPointInWall(PVector gridPt) {
    boolean withinX = gridA.x <= gridPt.x && gridPt.x < gridB.x;
    boolean withinY = gridA.y <= gridPt.y && gridPt.y < gridB.y;
    return withinX && withinY;
  }
}

class Serpent {
  PVector currentDir;
  PVector nextDir;
  ArrayList<SerpentPart> parts;
  boolean isAlive;

  Serpent(PVector start, int length) {
    isAlive = true;
    currentDir = RIGHT;
    nextDir = RIGHT;
    parts = new ArrayList<SerpentPart>();
    for (int ix = 0; ix < length; ix++) {
      PVector offset = LEFT.copy().mult(ix);
      parts.add(new SerpentPart(start.copy().add(offset)));
    }
  }

  void setDirection(PVector newDir) {
    PVector sum = newDir.copy().add(currentDir);
    if (sum.x != 0 && sum.y != 0) {
      nextDir = newDir;
    }
  }

  void nextStep(Walls walls, Food food) {
    currentDir = nextDir;
    SerpentPart nextHead = parts.get(0).offsetCopy(currentDir);
    if (nextHead.getPos().dist(food.getPos()) == 0) {
      food.eat();
    } else {
      parts.remove(parts.size() - 1);
    }
    checkCollisions(nextHead.getPos(), walls);
    parts.add(0, nextHead);
  }

  private void checkCollisions(PVector head, Walls walls) {
    if (walls.isPointInWalls(head) || isPointInSnake(head)) {
      isAlive = false;
      return;
    }
  }

  boolean isPointInSnake(PVector point) {
    for (int i = 0; i < parts.size(); i++) {
      if (parts.get(i).getPos().dist(point) == 0) {
        return true;
      }
    }
    return false;
  }

  boolean isDead() {
    return !isAlive;
  }

  void draw() {
    int ix =  0;
    for (SerpentPart part : parts) {
      part.draw();
      part.drawIndex(ix);
      ix++;
    }
  }
}

class GridPoint {
  PVector gridCoord;
  PVector drawCoord;
  GridPoint (PVector gridCoord) {
    this.gridCoord = gridCoord;
    this.drawCoord = pixelCoord(gridCoord);
  }
  final PVector getPos() {
    return gridCoord;
  }
}

class SerpentPart extends GridPoint {
  PVector textCoord;

  SerpentPart (PVector gridCoord) {
    super(gridCoord);
    this.textCoord = drawCoord.copy().add(3, 8);
  }

  void draw() {
    fill(Color.SERPENT);
    rect(drawCoord.x, drawCoord.y, GRID_WIDTH, GRID_WIDTH, 4);
  }

  void drawIndex(int ix) {
    fill(Color.SERPENT_TEXT);
    textSize(8);
    text(ix, textCoord.x, textCoord.y);
  }

  SerpentPart offsetCopy(PVector offset) {
    return new SerpentPart(gridCoord.copy().add(offset));
  }
}

class Food extends GridPoint {
  boolean isEaten = false;

  Food(PVector gridCoord) {
    super(gridCoord);
  }
  void eat() {
    isEaten = true;
  }

  boolean isEaten() {
    return isEaten;
  }

  void draw() {
    fill(Color.FOOD);
    rect(drawCoord.x, drawCoord.y, GRID_WIDTH, GRID_WIDTH, 5);
  }
}
