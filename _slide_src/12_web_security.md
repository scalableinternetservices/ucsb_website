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
