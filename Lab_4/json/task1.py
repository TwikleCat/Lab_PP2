import json

with open(r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_4\json\sample-data.json") as f:
    data=json.load(f)

print("interface status")
print(100*"=")
print(f"{'DN':<50}{'Description':<30}{'Speed':<10}{'MTU':<10}")
print(100*"-")

for inter in data.get("imdata", []):
    attribute=inter["l1PhysIf"]["attributes"]
    dn=attribute["dn"]
    description=attribute["descr"]
    speed=attribute["speed"]
    mtu=attribute["mtu"]

    print(f"{dn:<50} {description:<30} {speed:<10} {mtu:<10}")
