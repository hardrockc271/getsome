from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

@app.route("/")
def hello_world():
  query_parameters = request.args

  print("parms = ")
  print(query_parameters)

  calories = query_parameters.get('calories')
  ingredient = query_parameters.get('ingredient')

  print(calories)
  print(ingredient)

  query = "SELECT * from recipes WHERE"
  to_filter = []

  if calories:
    query += ' calories<=? AND'
    to_filter.append(calories)
  if ingredient:
    query += ' ingredients=? AND'
    to_filter.append(ingredient)

  print(query)

  print(to_filter)

  conn = sqlite3.connect('recipes.db')
  conn.row_factory = dict_factory
  cursor = conn.cursor()

  query_results = cursor.execute(query, to_filter).fetchall())

  zach_results = zachAlgorith(query_results)
  return jsonify(zach_results)

  return jsonify(value1=calories, value2=ingredient)

#  return "Hello, Rockwall!"

