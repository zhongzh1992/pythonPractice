from py2neo import Database, Graph

# 建立连接
db = Database("http://116.62.17.253:17474")
graph = Graph("bolt://116.62.17.253:17687", username="neo4j", password="neo4j4ai")

ans = graph.run('match(p) return p').to_ndarray()
print(ans)



