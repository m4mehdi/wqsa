import subprocess


def Delay(ip):
    '''Calculates the Delay and Jitter'''
    command = 'curl -o /dev/null -s -w %{time_connect}  '+ ip
    response = []
    for i in range(10):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        response.append(float(out)*1000)
    diff = [response[i] - response[i-1] for i in range(1,len(response))]
    diff = [abs(i) for i in diff]
    diff = [i for i in diff if i > 0]
    jitter = sum(diff)/len(diff)
    delay = sum(response)/len(response)
    return delay, jitter


def Response(ip):
    '''Calculates the Response Time'''
    command = 'curl -o /dev/null -s -w %{time_total}  '+ ip
    response_time = []
    for i in range(3):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        response_time.append(float(out)*1000)
    response_time = sum(response_time)/len(response_time)
    return response_time 
