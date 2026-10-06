# 🎯 Switch Track — CS Core (interview fundamentals)

**Goal:** pass the CS-fundamentals rounds (OS, DBMS, CN, OOP) and SQL rounds that Microsoft, Amazon, Google,
Uber, Atlassian, Adobe, Oracle, Flipkart and similar product companies run, at a depth that survives
follow-ups — the fastest route to the 30–35 LPA switch, without cutting anything (the rest is taught in the
depth pass, never deleted).
**Budget:** ~60 h · **Track total (est.):** ~62 h (57 h sessions + ~5 h targeted reading; the depth track
adds the remaining ~1,440 h over time).

**How it runs:** `progress/STATUS.md` has `**Active track:** switch`. `/today` walks this table in order.
`Scope` says what the switch pass covers now and what waits for the depth pass; a row is marked 🟨 when its
switch scope is done and re-opened at `full` scope when the depth track reaches it. After the last row here,
`/today` switches to the depth track and continues with the first roadmap row not yet done, in phase order.

## Order

| # | ID | Type | Topic | Scope | Est h |
|---|---|---|---|---|---|
| 1 | 0.0.1 | Intake | Intake & targets | full | 1.5 |
| 2 | 0.0.2 | Baseline | Sealed baseline CS viva | full | 1.5 |
| 3 | 4.1.1 | L | Process abstraction & states | full | 1.5 |
| 4 | 4.1.5 | C | Process vs thread vs coroutine | full | 1.25 |
| 5 | 4.1.3 | DD | Context switches | switch: what's saved, direct vs indirect cost, thread vs process; kernel switch_to source walk waits | 1.5 |
| 6 | 4.2.1 | L | Scheduling: FCFS, SJF, SRTF, RR, priority | full | 1.5 |
| 7 | 4.2.7 | WE | Scheduling numericals (Gantt charts) | full | 1.25 |
| 8 | 5.1.3 | L | Paging & page tables | full | 1.5 |
| 9 | 5.1.4 | DD | TLBs & EAT | switch: hit/miss, EAT, TLB reach, context-switch flush; shootdown depth waits | 1.5 |
| 10 | 5.2.2 | L | Page replacement (FIFO/LRU/OPT/clock, Belady, thrashing) | full | 1.5 |
| 11 | 6.1.2 | L | Locks: spinlock vs mutex, CAS, ticket lock | switch: correctness, spin vs sleep, CAS; futex internals in 6.1.3 wait | 1.5 |
| 12 | 6.2.2 | L | Semaphores & producer–consumer | full | 1.5 |
| 13 | 6.3.2 | DD | Deadlock: conditions, prevention, avoidance (banker's), detection | full | 1.75 |
| 14 | 10.1.1 | L | Relational model & keys | full | 1.25 |
| 15 | 10.2.1 | L | SQL semantics & joins | full | 1.5 |
| 16 | 10.2.3 | L | Subqueries & CTEs (incl. recursive) | full | 1.5 |
| 17 | 10.2.4 | DD | Window functions | full | 1.75 |
| 18 | 10.2.5 | LAB | SQL problem set I (classics, timed) | full | 2.5 |
| 19 | 10.2.6 | LAB | SQL problem set II (windows, recursion, islands) | full | 2.5 |
| 20 | 10.3.3 | DD | Normalisation 1NF–BCNF | full | 1.75 |
| 21 | 11.4.3 | L | ACID, isolation levels, anomalies & 2PL | switch: ACID, isolation levels & anomalies, 2PL/strict, deadlock handling; T/O, OCC, MVCC internals, precedence-graph proofs wait (11.4.1–2, 11.4.4–5) | 1.75 |
| 22 | 11.2.2 | DD | Indexes & B+ trees (and why not hash/BST) | switch: B+ tree shape, height, clustered vs secondary, when indexes don't help; split/merge internals & LSM wait | 1.75 |
| 23 | 8.1.2 | C | OSI vs TCP/IP layers & devices | full | 1.25 |
| 24 | 8.3.2 | DD | TCP: reliability, flow & congestion control | switch: handshake, reliability, flow vs congestion, TIME_WAIT, TCP vs UDP (SD switch covers this at design level — go one level deeper on RTO/AIMD); rdt derivation, GBN/SR, BBR internals & numericals wait (8.3.3–8.3.8) | 1.75 |
| 25 | 9.1.2 | L | IP addressing, CIDR & subnetting | full | 1.5 |
| 26 | 9.2.1 | L | Routing: link-state vs distance-vector | switch: LS/DV, Dijkstra & Bellman-Ford, count-to-infinity; OSPF/BGP depth waits (9.2.2–9.2.3) | 1.5 |
| 27 | 9.3.2 | L | Switched LANs: ARP, switches, VLANs, switch vs router vs hub | full | 1.5 |
| 28 | 9.3.5 | TR | Day in the life of a web request | switch: the end-to-end narrative (DHCP→ARP→DNS→TCP→TLS→HTTP→routing); the packet-capture lab (9.3.6) waits | 1.5 |
| 29 | 12.1.1 | L | OOP fundamentals with mechanism | full | 1.5 |
| 30 | 12.1.3 | DD | Virtual functions & vtables | switch: vtable/vptr dispatch, virtual destructor, ctor-time dispatch, cost; MI/RTTI depth in 12.1.4 waits | 1.75 |
| 31 | 12.2.1 | L | RAII, rule of 0/3/5, move semantics, smart pointers | full | 1.5 |
| 32 | 13.6.1 | L | The quantum threat (Shor vs Grover) | switch: résumé-relevant awareness (why PQC, harvest-now-decrypt-later); lattice/ML-KEM/QKD depth waits (13.6.2–13.6.6) | 1.25 |
| 33 | 15.2.1 | V | OS rapid-fire viva | full | 1.25 |
| 34 | 15.2.2 | V | DBMS rapid-fire viva (+ live SQL) | full | 1.5 |
| 35 | 15.2.3 | V | Networks rapid-fire viva | full | 1.25 |
| 36 | 15.3.1 | V | Company mock: mixed fundamentals | full | 1.5 |
| 37 | 15.3.6 | Baseline | Baseline redo (sealed) — measure the switch | full | 1.5 |

**Not on the switch track but usually already covered by the System Design switch track at interview level**
(so not repeated here; taught in this course's depth pass for mechanism): CAP/consistency intuition,
DNS resolution & records, HTTP versions & CDN/caching, load balancing, replication & sharding, NoSQL choice,
key-value/object storage. Where a fundamentals round probes the *mechanism* under these (e.g. how TCP is
actually reliable, how an index physically works), rows 22 and 24 add the extra depth.

## Deferred to the depth pass (not deleted)

| ID(s) | Topic | Why deferred |
|---|---|---|
| 0.1.x | Stack of abstractions, ./hello trace, numbers, toolbench | Foundational context, not asked directly in fundamentals rounds |
| 1.1–1.3 | Data representation, IEEE 754, x86-64, stack, buffer overflows | Machine-level depth; only overflow/undefined-behaviour awareness surfaces in interviews (covered indirectly via C++ rows) |
| 2.1–2.4 | Pipelining, branch prediction, caches, coherence, SIMD, perf | Performance-engineering depth; the "why is my loop slow past 8 MB" story is a bonus, not a fundamentals-round staple |
| 3.1–3.3 | Linking, loading, ELF, ECF, signals, Unix I/O | Systems-programming depth; fork/exec/signals asked occasionally (depth pass) |
| 4.1.2, 4.2.2–4.2.6 | LDE, MLFQ, lottery/stride, CFS/EEVDF, multiprocessor scheduling | Beyond the FCFS/SJF/RR/priority core that rounds ask |
| 5.1.1–5.1.2, 5.1.5–5.1.6, 5.2.1, 5.2.3, 5.3.x | Segmentation, multi-level tables, malloc internals, mmap/COW, huge pages, NUMA | VM depth beyond paging/TLB/replacement |
| 6.1.1, 6.1.3–6.1.4, 6.2.1, 6.2.3, 6.4.x | Threads/races, futexes, CV semantics, classical problems, memory model, lock-free | Concurrency depth beyond locks/semaphores/deadlock |
| 7.1–7.3 | Devices, HDD/SSD, RAID, file systems, journaling, fsync, epoll, containers, VMs | Persistence & Linux internals; container/VM and disk-scheduling asked in the depth pass |
| 8.1.1, 8.1.3–8.1.6, 8.2.x, 8.3.1, 8.3.3–8.3.10 | Delays, HTTP/DNS/CDN, sockets & servers, UDP, TCP internals, QUIC, numericals | Networking depth beyond the layering + TCP + reliability core |
| 9.1.1, 9.1.3–9.1.6, 9.2.2–9.2.5, 9.3.1, 9.3.3–9.3.8 | Fragmentation, router internals, NAT/IPv6, OSPF/BGP, ICMP/DHCP, link layer, wireless, packet labs | Networking depth beyond subnetting + routing basics + switching |
| 10.1.2–10.1.3, 10.2.2, 10.2.7–10.2.8, 10.3.1–10.3.2, 10.3.4–10.3.8 | Relational algebra, NULL/3VL depth, DDL/views/triggers, ER, FDs, 4NF, schema lab | DB design depth beyond keys/SQL/normalisation |
| 11.1.x, 11.2.1, 11.2.3–11.2.7, 11.3.x, 11.4.1–11.4.2, 11.4.4–11.4.8, 11.5.x | Storage, buffer pool, hashing, B+ tree/LSM internals, query processing/optimisation, CC theory, MVCC, WAL/ARIES, distributed DB, labs | Database-engine internals; the switch pass keeps only indexes/isolation/2PL at interview level |
| 12.1.2, 12.1.4–12.1.7, 12.2.2–12.2.6, 12.3.x, 12.4.x | Object layout, MI/RTTI, GC, type systems, the whole compiler pipeline & interpreter labs | Languages/compilers depth beyond the OOP/RAII/vtable core |
| 13.1–13.5, 13.6.2–13.6.6 | Crypto foundations, symmetric/asymmetric, TLS, vulnerabilities, PQC/QKD depth | Security depth beyond quantum-threat awareness (high value for QNu; front-loaded in the depth pass) |
| 14.x | Theory of computation (automata, decidability, NP-completeness) | Rarely in fundamentals rounds; done in the depth pass |
| 15.1.x, 15.2.4–15.2.9, 15.3.2–15.3.5, 15.3.7 | OOP/C++ & security vivas, SQL rounds, whole-stack traces, more company mocks | Extra interview drilling; add on demand near a real interview date |
