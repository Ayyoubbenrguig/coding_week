import torch
import torch.nn as nn
import numpy as np

class MatrixFactorization(nn.Module):

    def __init__(self,
                 num_users:int,
                 num_items:int,
                 num_factors:int,
                 device : torch.device,
                 use_bias=False,
                 use_confidence=False,) -> None:

        super(MatrixFactorization, self).__init__()
        self.num_users = num_users
        self.num_items = num_items
        self.num_factors = num_factors
        self.device = device
        self.use_bias = use_bias
        self.use_confidence = use_confidence

        self.user_embedding = nn.Embedding(self.num_users,self.num_factors) # num_users = classe of users +1
        self.item_embedding = nn.Embedding(self.num_items,self.num_factors) # num_items = classe of items +1
        torch.nn.init.ones_(self.user_embedding.weight)
        torch.nn.init.ones_(self.item_embedding.weight)

    def forward(self,users,items,bias_user,bias_item,o_avg,c_score):
        result = torch.bmm(self.user_embedding(users),torch.transpose(self.item_embedding(items),1,2))
        user_embedding = torch.squeeze(self.user_embedding(users))
        item_embedding = torch.squeeze(self.item_embedding(items))
        result = torch.mm(user_embedding, torch.transpose(item_embedding,1,0))
        result = torch.diagonal(result,0)
 
        if self.use_bias:
            bias = bias_user+ bias_item+ o_avg
            result = result+bias
        if self.use_confidence:
            result = torch.bmm(result,c_score)
        return result

    def __call__(self,*args):
        return self.forward(*args)

