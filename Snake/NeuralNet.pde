// author: "Code Bullet" (https://github.com/Code-Bullet/SnakeFusion/blob/master/SmartSnakesCombine/NeuralNet.pde)

class NeuralNet {

  int iNodes;
  int hNodes;
  int oNodes;

  Matrix whi;//matrix containing weights between the input nodes and the hidden nodes
  Matrix whh;//matrix containing weights between the hidden nodes and the second layer hidden nodes
  Matrix woh;//matrix containing weights between the second hidden layer nodes and the output nodes
  //---------------------------------------------------------------------------------------------------------------------------------------------------------  

  //constructor
  NeuralNet(int inputs, int hiddenNo, int outputNo) {

    //set dimensions from parameters
    iNodes = inputs;
    oNodes = outputNo;
    hNodes = hiddenNo;


    //create first layer weights 
    //included bias weight
    whi = new Matrix(hNodes, iNodes +1);

    //create second layer weights
    //include bias weight
    whh = new Matrix(hNodes, hNodes +1);

    //create second layer weights
    //include bias weight
    woh = new Matrix(oNodes, hNodes +1);  

    //set the matricies to random values
    whi.randomize();
    whh.randomize();
    woh.randomize();
  }
  //---------------------------------------------------------------------------------------------------------------------------------------------------------  

  //mutation function for genetic algorithm
  void mutate(float mr) {
    //mutates each weight matrix
    whi.mutate(mr);
    whh.mutate(mr);
    woh.mutate(mr);
  }

  //---------------------------------------------------------------------------------------------------------------------------------------------------------  
  //calculate the output values by feeding forward through the neural network
  float[] output(float[] inputsArr) {

    //convert array to matrix
    //Note woh has nothing to do with it its just a function in the Matrix class
    Matrix inputs = woh.singleColumnMatrixFromArray(inputsArr);

    //add bias 
    Matrix inputsBias = inputs.addBias();


    //-----------------------calculate the guessed output

    //apply layer one weights to the inputs
    Matrix hiddenInputs = whi.dot(inputsBias);

    //pass through activation function(sigmoid)
    Matrix hiddenOutputs = hiddenInputs.activate();

    //add bias
    Matrix hiddenOutputsBias = hiddenOutputs.addBias();

    //apply layer two weights
    Matrix hiddenInputs2 = whh.dot(hiddenOutputsBias);
    Matrix hiddenOutputs2 = hiddenInputs2.activate();
    Matrix hiddenOutputsBias2 = hiddenOutputs2.addBias();

    //apply level three weights
    Matrix outputInputs = woh.dot(hiddenOutputsBias2);
    //pass through activation function(sigmoid)
    Matrix outputs = outputInputs.activate();

    //convert to an array and return
    return outputs.toArray();
  }
  //---------------------------------------------------------------------------------------------------------------------------------------------------------  
  //crossover function for genetic algorithm
  NeuralNet crossover(NeuralNet partner) {

    //creates a new child with layer matrices from both parents
    NeuralNet child = new NeuralNet(iNodes, hNodes, oNodes);
    child.whi = whi.crossover(partner.whi);
    child.whh = whh.crossover(partner.whh);
    child.woh = woh.crossover(partner.woh);
    return child;
  }
}
