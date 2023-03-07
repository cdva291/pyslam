# pySLAM2 Virtual Environment 

The following instructions allow you to create a custom `pyslam` virtual environment by using the package `python3-venv`. You will be able to run pyslam scripts within such environment. 

## Basic Installation 

In order to run `main_vo.py` with venv, get in the root of this repository and run the following command:
```
$ . pyenv-create.sh 
```
**N.B.**: do not forget the dot! (without '/' !)

This will create a custom `pyslam` environment and will also activate it. Now, from the same terminal, you can run: 
```
$ python3 -O main_vo.py
```
If you want to use a new terminal, you need to activate the `pyslam` environment as explained in this [section](#activate-the-created-pyslam-environment)
 
If you are under **macOS**, please check this [document](./MAC.md).

## Full Installation 

In order to run `main_slam.py` with venv, get in the root of this repository and run the following command:
```
$ . install_all_venv.sh  
```
**N.B.**: do not forget the dot! (without '/' !)

This will compile the required thirdparty packages and will also activate the created `pyslam` environment. Now, from the same terminal, you can run: 
```
$ python3 -O main_slam.py
```
If you want to use a new terminal, you need to activate the `pyslam` environment as explained in this [section](#activate-the-created-pyslam-environment)


## Create a `pyslam` python virtual environment 

You already see this above. In order to create a custom `pyslam` python virtual environment, get in the root of this repository and run the following command: 
```
$ . pyenv-create.sh 
```
**N.B.**: do not forget the dot! (without '/' !)

This will create and activate a python virtual environment `pyslam` where to safely run pyslam scripts. 

## Activate the created `pyslam` environment 

Run the following command: 
```
$ . pyenv-activate.sh 
```
Now, you can launch pySLAM scripts. 

## Deactivate `pyslam` environment 

Run the command: 
```
$ deactivate 
```

## Delete `pyslam` environment 

To delete the `pyslam` environment, run
```
$ . pyenv-delete.sh 
```


--- 
# General Notes About Python Virtual Environments 

Below, you can find some useful details. The scripts mentioned above make the work for you. 

## Install virtualenv package 

```
sudo apt install python3-venv
```

## Where to create a new virtual environment 

You can create a new directory where to deploy the new environment with name `venv-name`
```
$ mkdir -p ~/.python/venvs/<venv-name> 
$ cd ~/.python/venvs/<venv-name>
```
Create a new virtual environment inside the directory:
```
$ python3 -m venv <venv-name>
```

## Activate the environment 

In order to use this environment’s packages/resources in isolation, you need to “activate” it. To do this, just run the following:

```
$ source ~/.python/venvs/<venv-name>/bin/activate
```
This will return in your shell a prefixed prompt with the name of your environment
```
(env) $
```
This is the indicator that env is currently active, which means the python executable will only use this environment’s packages and settings.


## Deactivate the environment 

Run the following command 
```
(env) $ deactivate
```
This will removed the prefixed prompt. 

## Install packages from requirements.txt 

You can generate a `requirements.txt` file by running: 
```
$ pip3 freeze > requirements-pip3.txt 
``` 
You can install from such a file by runnning: 
```
$ pip3 install -r requirements-pip3.txt
```

**N.B.**: the file `requirements.txt` generated by pip3 cannot be used with conda (and viceversa)! 

## Check if you are in an activated virtual environment 

From shell check the shell prefix, as explained above 

From a script, you can use the following code:
```
function get_after_last_slash(){
    ret=$(echo $1 | sed 's:.*/::')
    echo $ret 
}
function get_virtualenv_name(){
    cmd_out=$(printenv | grep VIRTUAL_ENV)
    virtual_env_name=$(get_after_last_slash $cmd_out)
    echo $virtual_env_name
}
```
the function `get_virtualenv_name` returns the name of the path of the activated virtual environment. 
If no virtual environment has been activated then the output will be empty.  



## Links 

* https://realpython.com/python-virtual-environments-a-primer/  (first and clear reference)