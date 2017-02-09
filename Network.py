#coding=utf-8
import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:])]
    

if __name__ == "__main__":
    net = Network([2, 3, 1])
    #print np.zeros(net.biases[1].shape)
    print net.biases
    print net.weights

    nabla_b = [np.zeros(b.shape) for b in net.biases]
    nabla_w = [np.zeros(w.shape) for w in net.weights]

    print nabla_b
    print nabla_w