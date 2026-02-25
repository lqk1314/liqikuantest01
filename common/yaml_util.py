import os.path

import yaml


def get_path():
    current_dir=os.path.dirname(os.path.abspath(__file__))
    project_root=os.path.dirname(current_dir)
    return project_root

def read_yaml(yamlpath,key):
    full_path=os.path.join(get_path(),yamlpath)
    with open(full_path,mode='r',encoding='utf-8') as f:
        data=yaml.load(stream=f,Loader=yaml.FullLoader)
        items=data.get(key,[])
        result=[]
        for item in items:
            data_tuple=(key,)+tuple(item.values())
            result.append(data_tuple)
        return result


if __name__=='__main__':
    print(read_yaml('testcases/test_web.yaml',"web_log"))
    print(read_yaml('testcases/test_web.yaml',"web_day"))
