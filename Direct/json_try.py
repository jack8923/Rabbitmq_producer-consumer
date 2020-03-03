import ast
import json

j_string = '''{
  "orderId" : "adfafdafafdasfas",
  "products" : [{
    "name" : "abc" ,
    "price" : 1010
  },
  {
    "name" : "abc1" ,
    "price" : 10101
  }],
  "receipient" : {
    "basicProfile" : {
        "name" : "",
        "phoneNumber" : "",
        "email" : "",
    },
    "addresses" : [{
        "addressType" : "billing",
        "line1" : "",
        "line2" : "",
        "city" : "",
        "state" : "",
        "country" : ""
    },{
        "addressType" : "delivery",
        "line1" : "",
        "line2" : "",
        "city" : "",
        "state" : "",
        "country" : ""
    }]
 }
}'''

data = ast.literal_eval(j_string)
# data = json.loads(j_string)

#print(type(data))
# print(data)
# print(data['recipient']["basicProfile"])
#import json

class User:

    def __init__(self, orderId, products, receipient):
        self.orderId = orderId
        self.products = products
        self.receipient = receipient

    @classmethod
    def convert(cls, str):
        return cls(**eval("dict({})".format(str)))


user = User.convert(j_string)
j_user = json.dumps(user.__dict__)

print(type(data))

