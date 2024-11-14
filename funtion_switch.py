import subprocess
import json

def test_help1():
    result=subprocess.run(['chef-node-management-cli','management','skill','find-all-skills'],capture_output=True,text=True)
    print(result.stdout)
    try:
        res = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return
    print(res)
    skillname = res["item"]["name"]
    print(skillname)
    assert result.returncode==0

print("1->Courier Runner skill\n2->Gohai skill\n3->Shell interpreter skill\n4->Shell interpreter skill\n5->Chef Client interpreter skill")
value =int(input())
if value == '1':
    result1=subprocess.run(['chef-node-management-cli','management','skill','courier-runner'],capture_output=True,text=True)
    print(result1.stdout)
    assert result1.returncode==0
elif value == '2':
    result1=subprocess.run(['chef-node-management-cli','management','skill','chef-gohai'],capture_output=True,text=True)
    print(result1.stdout)
    assert result1.returncode==0        
elif value == '3':
    result1=subprocess.run(['chef-node-management-cli','management','skill','courier-runner'],capture_output=True,text=True)
    print(result1.stdout)
    assert result1.returncode==0
elif value == '4':
    result1=subprocess.run(['chef-node-management-cli','management','skill','inspec-interpreter'],capture_output=True,text=True)
    print(result1.stdout)
    assert result1.returncode==0
elif value == '5':
    result1=subprocess.run(['chef-node-management-cli','management','skill','node-management-agent'],capture_output=True,text=True)
    print(result1.stdout)
    assert result1.returncode==0
else:
    print("Default Option") 
