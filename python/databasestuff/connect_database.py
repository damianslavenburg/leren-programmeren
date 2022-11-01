from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


cloud_config= {
         'secure_connect_bundle': 'C:/Users/Damian/Documents/leren-programmeren/python/databasestuff/secure-connect-signup.zip'
}
auth_provider = PlainTextAuthProvider('ckjSgHZotmWyYFbJXRYYcYxU', 'FwJ1SjYdckK26ur43yzeZJQci5uvXzffDF1z31P+E-zBlQFNbNARf.pvEw8YA33A2Q1+XhJOxeq9Y1DqM4n1HK.,_mo2sZ1zTqlQnoeSdnKgm74Z,6BIR70+AKdN.k+J')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
      print(row[0])
else:
      print("An error occurred.")