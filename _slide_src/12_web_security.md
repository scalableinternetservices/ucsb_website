# An Introduction to Web Security
.fx: title

__CS290B__

Dr. Bryce Boe

November 5, 2015

---

# Today's Agenda

* Security Motivation
* HTTPS
* Firewalls
* SQL Injection
* Cross-Site Scripting
* Cross-Site Request Forgery

---

# Security Motivation

Internet services increasingly mediate more and more interactions in modern
society.

* I want to buy dinner.
* I want to save important documents.
* I want to find a job.
* I want to manage my investments.

Every day billions of people use the same suite of technologies to solve these
problems.

> How do we keep these interactions secure?

---

# Malice Online

> What sort of _bad actors_ can exist in this system?

![Browser to Client](img/no_malicious_users.png)

---

# Malicious Client

A malicious client may be a compromised host (browser, server, operating
system), or a direct attacker.

![Malcious Client](img/malicious_client.png)

---

# Malicious Server

A malicious server may be impersonating a real server (therealgoogle.com) in
attempt to phish unsuspecting users, or it could be a compromised high-traffic
web service serving up drive-by-downloads.

![Malcious Server](img/malicious_server.png)

---

# Malicious Observer

A malicious observer may be your neighbor or even your government NSA that is
recording your actions for nefarious purposes such as obtaining sensitive
information (credentials, bank account numbers, credit cards), blackmail
(ransomware).

![Malcious Observer](img/malicious_observer.png)

---

# Malicious Intermediary

A malicious intermediary is similar to a malicious observer, but requires more
than passive collection of web traffic. Intermediaries may perform a
man-in-the-middle attack, DNS poisioning, or a handful of other types of
attacks.

![Malcious Intermediary](img/malicious_intermediary.png)

---

# Online Security Goals

> What do we want?

## Privacy

My data cannot be read by by third parties.

## Authenticity

I am communicating with whom I expect to be communicating with.

## Integrity

Neither my messages, nor the other party's messages have been tampered with.

---

# HTTPS

HTTP over TCP with a _trusted_ TLS session (HTTPS) is designed to protect us
against malicious __servers__, __observers__, and __intermediaries__.

![Malicious Users](img/malicious_intermediary.png)

---

# Problems with TCP

Just using TCP as our transport-level protocol gives us little-to-no
protection.

Anyone on the path of the TCP stream (routers, switches, other clients on a
wireless network) can:

* Read the packets (violates privacy)
* Inject _fake_ packets to disrupt the stream or impersonate the destination
  server (violates authenticity)
* Inject modified packets to change their meaning (violates integrity)

---

# Solution to our Goals: Cryptography

---

# Cryptography in a Nutshell

## Symmetric Cryptography (fast)

Uses a single key to encrypt and decrypt data.

    encrypt(data, key) = encrypted               decrypt(encrypted, key) = data

Common implementations: __AES__, __DES__, __Threefish__

## Asymmetric Cryptography (slow in practice)

Uses a pair of keys, one public (pub_key), and one private (priv_key). Either
key can be used to encrypt data, and the other used to decrypt.

    # Only those with the private key can decrypt
    encrypt(data, pub_key) = encrypted      decrypt(encrypted, priv_key) = data

    # Only those with the private key can create
    encrypt(data, priv_key) = encrypted      decrypt(encrypted, pub_key) = data

Common implementations: __RSA__, __RSA__

---

# Symmetric Cryptography and Requests

![HTTP with Symmetric Cryptography](img/http_with_crypto.png)

> How far can symmetric cryptography alone get us?

---

# Symmetric Cryptography and Requests

![HTTP with Symmetric Cryptography](img/http_with_crypto.png)

> How far can symmetric cryptography alone get us?

__Privacy__: Without the key both the requests and the responses are
unreadable.

__Integrity__: Assuming no intermediary has the secret key, the data we decrypt
is guaranteed to be the data that was encrypted on the server-side.

Authenticity: We have no guarantee that we are actually communicating
with whom we intend to be. :(

---

# Supporting Authenticity on the Web

It is desirable for the web to work with combinations of arbitrary clients and
servers. As a result we cannot rely upon shared secrets for communication
between our browser and whatever server we want to talk to.

> How do we establish a shared symmetric key without intermediaries knowing it?

---

# Asymmetric Cryptography on the Web

Use asymmetric crypto to communicate a shared secret key.

![HTTP Shared Secret](img/http_shared_secret.png)

> Does this solve all of our malicious actor problems?

---

# Man in the Middle Attack

Malicious itermediary can:

* Create their own asymmetric key pair
* Present their public key to the server as the client's public key
* Establish a shared key with the server
* Present their public key to the client as the server's public key
* Establish a shared key with the client
* Relay messages between the client and server, modifying them as desired

> How can we prevent a man in the middle attack?

---

# Preventing Man in the Middle Attack

If one side knew in advance the public key of the other side, the man in the
middle attack wouldn't work.

__The attacker is unable to decrypt one of the messages containing half of the
secret key.__

> Can the server know in advance the public key belonging to a client (e.g.,
> browser)?

> Can the the client know in advance the public key belonging to a server?

> How?

---

# Establishing Trust

There are significantly more clients than web servers so it makes sense to
focus on advanced knowledge of server public keys.

> Where can we store the public keys?

* The server?
* DNS?
* Trusted Central Authority?

All of these have the same problem.

> How can we trust that the transmission of the desired server's public key has
> not been tampered with?

---

# A Web of Trust

We can use public key signatures to transitively authenticate someone.

* Alice trusts Bob and as a result already has Bob's public key.
* Bob trusts Chelsea and has even _signed_ Chelsea's public key.
* Alice doesn't know Chelsea but wants to talk to him.
    * Alice asks Chelsea for his public key.
    * Chelsea presents his public key along with the signature from Bob.
    * Alice verifies that Chelsea's key has indeed been signed with Bob's key,
      someone she trusts, and as a result accepts that she is really talking to
      Chelsea.

The public key along with it's parent signatures is known as a __certificate__.

---

# Certificate Authorities (CAs)

Every browser (and operating system) maintains a small list of trusted
Certificate Authorities.

Any website can present a certificate issued (signed) by a CA the browser
trusts and transitively the browser will trust that website.

Certificates can be chained (Root CA -> Intermediate CA -> Site Certificate)

![TLS Certificate Chain](img/certificate_chain.png)

---

# Trust Summary

* __Certificates__ are used to verify the _authenticity_ of the sever.
* __Asymmetric cryptography__ is used to establish a shared key.
* __Symmetric cryptography__ is used to _privately_ communicate with
  _integrity_.

The TLS layer added on-top of a TCP session provides all this functionality
with different combinations of cipher suites.

---

# TLS Handshake

.fx: img-left

![TLS Handshake](img/tls_handshake.png)

## After TCP setup

1. Client initiates TLS handshake with a list of CipherSuites and a random
   number
2. Server responds with its cert, selected CipherSuite, and a random number
3. Client responds with more randomness, encrypted with the server's public key
4. Each side computes session key based on the three random numbers
5. Both sides use the symmetric session key to communicate

---

# Minimizing Round Trips

.fx: img-left

![TLS Handshake](img/tls_handshake.png)

The latency involved in the two extra round trips is expensive!

For access from a client to a previously accessed server, there exists an
optimization.

---

# Abbreviated TLS Handshake

.fx: img-left

![Abbreviated TLS Handshake](img/abbreviated_tls_handshake.png)

## After TCP setup

1. Session ID is added to connections with new hosts
2. Client initiates TLS handshake with previously-used session ID
3. Server acknowledges previously used session ID
4. Each side computes session key based on remembered random numbers
5. Both sides use the symmetric session key to communicate

---

# TLS Goals

> Have we acheived our goals?

## Privacy

No other party can know the three random numbers with which we generated the
session key, thus intermediaries cannot read our data.

## Integrity

Each TLS frame includes a Message Authentication Code (MAC) that ensures
messages were not tampered with.

## Authentication

The server's public key is signed (certificate) by a trusted CA that my browser
already knows about, thus I am certainly communicating with the intended party.

---

# TLS Certificate Revocation

> What happens if a server's private key is compromised or an intermediate CA
> becomes untrustworthy

Certificates can be revoked by two primary ways:

* Certificate Revocation List
    * Periodically fetch a list of all revoked certificates.
    * At request time, reject revoked server certificates.
* Online Certificate Status Protocol (OCSP)
    * At request time, use OCSP to see if the server's certificate has been
      revoked. If so reject it.

> What are the trade-offs of the two approaches?

---

# Terminating TLS

> Where should TLS connections terminate?

At the Application Server
![App Server TLS Termination](img/tls_termination_app_server.png)

At the Load Balancer
![Load Balancer TLS Termination](img/tls_termination_load_balancer.png)

---

# TLS Termination Options

## Advantages of termination at the Load Balancer

* Minimizing the number of TLS session caches improves hit rate of the
  abbreviated TLS handshake
* Easier to provide TLS hardware acceleration (less hardware required)
* Enables the load balancer to make decisions based on content
* Single location for private key

## Advantages of termination at the App Server

* Data between load balancer and app server stays private (do you trust the
  network between the load balancer and your application servers?)

---

# HTTPS Strict Transport Security

HTTP over TCP+TLS (HTTPS) gives us very good security for the web. However,
users aren't always aware it is an option, or may be _coerced_ into using just
HTTP.

> How can we enforce that browsers access our site using only HTTPS?

Strict Transport Security gives us the option to inform the browser that for
all future communication to use HTTPS.

__HTTP Response Header__:

    Strict-Transport-Security: max-age=31536000

Informs the browser to only use HTTPS to access the domain for the next year.

---

# Common Web Vulunerabilties

Now we will look at three common security vulnerabilities on the web and how to
mitigate them:

## SQL Injection

Attacker can execute arbitrary SQL on the database

## Cross-site Scripting

Attacker can execute arbitrary javascript on a user's browser

## Cross-site Request Forgery

Attacker can trick user into performing an action on a targeted site

---

# SQL Inejection

An SQL injection attack is when a malicious user submits a carefully crafted
HTTP request that directly or indirectly causes your application server to
interact with the database in a manner you did not indend.

---

# SQL Injection Example

> How could we maniuplate the following controller?

    !ruby
    def create
      sql = <<-SQL
        INSERT INTO comments
        user_id=#{params['user_id']},
        comment=#{params['comment_text']}
      SQL
      ActiveRecord::Base.connection.execute(sql)
    end

---

# SQL Injection Example

    !ruby
    def create
      sql = <<-SQL
        INSERT INTO comments
        user_id=#{params['user_id']},
        comment=#{params['comment_text']}
      SQL
      ActiveRecord::Base.connection.execute(sql)
    end


> What if a user submitted the following parameters?

    user_id=5
    comment_text='; UPDATE users SET admin=1 WHERE user_id=5 and '1'='1

---

# SQL Injection Example

What was templated as:

    !sql
    INSERT INTO comments user_id=#{user_id}, comment='#{comment_text}'

will become:

    !sql
    INSERT INTO comments user_id=5, comment='';
    UPDATE users SET admin=1 WHERE user_id=5 and '1'='1'

---

# Mitigating SQL Injection Vulnerabilities

Never insert user input directly into an SQL statement without sanitizing it
first.

Rails does a lot of the work here for you:

* Access through the ActiveRecord ORM is safe
* If you need to sanitize custom SQL, use the `sanitize` method:

        !ruby
        "SELECT * FROM comments WHERE id=#{Comment.sanitize(params[:id])};"

---

# XKCD: Exploits of a Mom

![XKCD Little Bobby Tables](img/xkcd_327.png)

"Her daughter is named Help I'm trapped in a driver's license factory."

(C) Randall Munroe: [http://xkcd.com/327/](http://xkcd.com/327/)

---

# References

Slide images from "High Performance Browser Networking":

* "Certificate Authorities (CAs)"
* "TLS Handshake"
* "Abbreviated TLS Handshake"
