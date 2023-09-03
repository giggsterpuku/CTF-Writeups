### Challenge: actually-proxed

#### Category: web

#### Description: Still cool haxxorz only!!! Except this time I added in a reverse proxy for extra security. Nginx and the standard library proxy are waaaayyy too slow (amateurs). So I wrote my own :D

#### Author: Jordan Bertasso

I first solved the challenge out of making an idea aobut the vulnerability, then I looked back at the source code to confirm where the vulnerability was. Going into this challenge, I knew from the supposedly prequel to this challenge "proxed" that the gist of that challenge was to mask your IP to be the desired one that the web server will give the flag to by filling in the HTTP request header field X-Forwarded-For with the desired IP address. Here, the server source code is the same:

```go
                // 1337 hax0rz 0nly!
                if ip != "31.33.33.7" {
                        message := fmt.Sprintf("untrusted IP: %s", ip)
                        http.Error(w, message, http.StatusForbidden)
                        return
                } else {
                        w.Write([]byte(os.Getenv("FLAG")))
                }
```

The only catch is that the HTTP request sent to the server first has to go to a proxy server, which is supposed to be a wall of defense to filter out any malicious content in the HTTP requests. I found that sending the same request from the "proxed" challenge didn't work, as I got the untrusted IP message signifying my request failed to get the flag. I tried looking into other header fields to try like X-HTTP-Forwarded-For, but those didn't work. However, I had an idea: since the proxy server filters out the HTTP requests going to the server, maybe it strips one instance of the X-Forwarded-For header field in the request so that the server sees the my IP address somehow. What if I send two X-Forwarded-For header fields so that if one field is stripped from the request, the other stays on? I tried it, and I got the flag. Great!

To confirm if my idea was actually correct, I looked at the proxy's source code and found this section of code:

```go
        for i, v := range headers {
                if strings.ToLower(v[0]) == "x-forwarded-for" {
                        headers[i][1] = fmt.Sprintf("%s, %s", v[1], clientIP)
                        break
                }
        }
```

It turns out that one of the X-Forwarded-For fields that I sent actually has its value replaced by my actual IP address, but it checks for ONLY ONE X-Forwarded-For header. Thus, the other one I sent stays intact, allowing me to pass the check in the server, so I was somewhat right.

Here is my cURL payload: curl proxed.duc.tf:30009 -H "X-Forwarded-For: 31.33.33.7" -H "X-Forwarded-For: 31.33.33.7"

#### Flag: DUCTF{y0ur_c0d3_15_n07_b3773r_7h4n_7h3_574nd4rd_l1b}

Solved by giggsterpuku
