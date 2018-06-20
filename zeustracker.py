import requests
import yaml
import os

inteltype = ['INTEL_URL','INTEL_ADDR','INTEL_DOMAIN']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/zuestracker/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def import_url_intel():
    try:
        source = cfg['enrichment_plugin']['ZUESTRACKER_URL_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '':
                tmp_dict = {}
                tmp_dict["EvtType"] = "URL"
                tmp_dict["EvtName"] = s
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["ZUESTRACKER"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                b_lst.append("ZuesC&C")
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_URL'


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['ZUESTRACKER_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '':
                tmp_dict = {}
                tmp_dict["EvtType"] = "IPv4"
                tmp_dict["EvtName"] = s
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["ZUESTRACKER"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                b_lst.append("ZuesC&C")
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_ADDR'


def import_domain_intel():
    try:
        source = cfg['enrichment_plugin']['ZUESTRACKER_DOMAIN_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '':
                tmp_dict = {}
                tmp_dict["EvtType"] = "DOMAIN"
                tmp_dict["EvtName"] = s
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["ZUESTRACKER"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                b_lst.append("ZuesC&C")
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_DOMAIN'
