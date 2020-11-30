"""
JSON format:
# JObject
{
	"a": 1,
  "b": 2
}

JArray
[1,2,3]
["a","b"]

JValue
1
"a"

Example:

{
	"a": [{"b":[]}, {"c": 2}]
}

# --- C# format of JSON ---
var str = @"
{
	"a": [{"b":[]}, {"c": 2}]
}";
var token = JToken.Parse(str);

Todo: write a function to implement JsonSerialization.
string Serialize(JToken token):
"""

# 使用递归来做。
def serialize(token):
  	if isinstance(token, str):
      	return "\"{}\"".format(token)
	elif isinstance(token, (int, float)):
    	# 如果是 JValue
    	return str(token)
    elif isintance(token, list):
    	# 如果是JArray
        array = []
        for subtoken in token:
        	array.append(serialize(subtoken))  
    	return "[" + ",".join(array) + "]"
    elif isinstance(token, dict):
      	# 如果是Jobject
		object_members = []
        # 保存每一条 `"a":1`
        for k, v in token.items():
          	object_members.append("\"{}\":{}".format(k, serialize(v)))
        return "{" + ",".join(object_members) + "}"

if __name__ == "__main__":
  	test_case =[]
  	json_object1 = {
      "a": [],
      "b": {},
      "c": 1,
      "d": {"a": 1}
    }
    test_case.append(json_object1)
    json_object2 = [1,2,3]
    test_case.append(json_object2)
    json_object3 = "a"
    test_case.append(json_object3)
    json_object4 = ["a","b","c"]
    test_case.append(json_object4)
    
    for test in test_case:
    	print(serialize(test))