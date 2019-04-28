Stats stats;
Stepper stepper;

Walls walls;
Serpent serpent;
Food food;
PVector startPosition = new PVector(30, 25);

void setup() {
  size(520, 520, FX2D);
  noStroke();
  stats = new Stats();
  stepper = new Stepper();

  walls = new Walls();
  serpent = new Serpent(startPosition, 8);
  food = createNewFood();
}

void draw() {
  stepper.step();
  background(245);

  walls.draw();
  serpent.draw();
  food.draw();
  stats.draw();
}

void keyPressed() {
  PVector dir = getKeyDirection();
  if (dir != null) {
    serpent.setDirection(dir);
  }
}

PVector getKeyDirection() {
  switch(keyCode) {
  case 0x26:
  case 0x57: 
    return UP;
  case 0x25:
  case 0x41: 
    return LEFT;
  case 0x28:
  case 0x53: 
    return DOWN;
  case 0x27:
  case 0x44: 
    return RIGHT;
  }
  return null;
}

Food createNewFood() {
  PVector point;
  while (true) {
    point = randomPoint();
    if (!walls.isPointInWalls(point) && !serpent.isPointInSnake(point)) {
      return new Food(point);
    }
  }
}

PVector randomPoint() {
  return new PVector(int(random(gridCoord(width))), int(random(gridCoord(height))));
}

class Stepper {
  int lastStep;
  Stepper() {
    lastStep = millis();
  }
  void step() {
    if (millis() - lastStep > 200) {
      lastStep = millis();
      serpent.nextStep(walls, food);
      if (food.isEaten()) {
        food = createNewFood();
      }
      if (serpent.isDead()) {
        noLoop();
        stats.gameEnd();
      } else {
        stats.nextStep();
      }
    }
  }
}
