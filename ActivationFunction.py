import numpy as np 

def sigmoidForward(x):
    '''
    this function does the forward pass of the sigmoid function
    it takes an input array i just called x 
    and it returns a tuple with the result (out) of the sigmoid function
    as well as cache which we use in the backward pass, its just the same as the out 
    '''
    out = 1/ (1+ np.exp(-x)) #the sigmoid function
    cache = out 
    return out, cache

def simoidBackward(dout, cache):
    '''
    does the backward pass of the simoid function
    i used d to show that its the derivative 
    so dx is the gradient of the loss with resepct to x (the input array)
    dout is the upstream gradient
    sig is just the sigmoid function hence why it equals cache
    '''
    sig = cache
    dx = dout * sig * (1 - sig) #the derivative of the sigmoid function multiplied by the upstream gradient to get the proper flow of gradients
    return dx

def reluForward(x):
    '''
    does the forward pass of the ReLU function
    x is the input arry 
    and then it outputs a tuple with the result of the  ReLU forward pass as well a cache used for backward pass
    cache this time is the input array 
    '''
    out = np.maximum(0,x)
    cache = x 
    return out, cache

def reluBackward(dout, cache):
    '''
    backward pass of the ReLU function
    x is just passing on the inpui arrat from forward pass using cache as the temporary store 
    dx is the gradient of the loss in respect to the input (being the array x)
    dout is the upstream gradient 
    '''
    x = cache 
    dx = dout * (x > 0) #derivative is 1 when x >0 otherwise it is 0
    return dx