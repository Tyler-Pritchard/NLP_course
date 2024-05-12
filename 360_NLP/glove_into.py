
import torch # type: ignore
import torchtext.vocab as vocab # type: ignore

glove = vocab.GloVe(name='6B', dim=100)

glove.vectors.shape