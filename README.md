[![Build Status](https://travis-ci.org/Kukmedis/py-simplecqrs.svg?branch=master)](https://travis-ci.org/Kukmedis/py-simplecqrs)
# Simple CQRS application in Python
### How it works

       X
      XXX                +------Projection------+
       X     Balance View|    Balance Sheet     |
    XXXXXXX  <-----------+"XX1"-------------1400+<-------------+
       X                 |"XX2"-------------2333|              |
       X                 |                      |              |
      XXX                +----------------------+              |
     XX XX                                                     |
    XX   XX  +-----------+                                     |
    X     X              |Deposit                              |
                         |                                     |
       +                 |                                     |
       |                 |                                     |
       |                 |                                     |
       |                 |                                     |
       |Withdraw         v                                     |
       |                 +------Bus/Handler-----+              |
       |                 |                      |              |
       +---------------->+    Account Handler   |              |New Events
                         |                      |              |
                         +--+----------------+--+              |
                            ^                |                 |
                            |                |                 |
                            |                |                 |
                Event Stream|                |New Events       |
                            |                |                 |
                            |                |                 |
                            |                |                 |
                            |                |                 |
                            |                v                 |
                      +-----+---Event-Store--+-----+           |
                      |AccountCredited "XX1", 1000 |           |
                      |AccountCredited "XX5", 2000 |           |
                      |AccountDebited  "XX1", 300  |           |
                      |AccountCredited "XX1", 100  +-----------+
                      |AccountDebited  "XX1", 200  |
                      |AccountCredited "XX5", 333  |
                      |............................|
                      +----------------------------+

### What is included
##### Event Store
Sample event store saves events into dictionary. Nice features:
+ Saves events
+ Loads event stream
+ Provides events for projection

Event store does not publish events - projections need to poll for new events themselves
##### Account Handler
Command Handler and Command Bus as one thing for the sake of simplicity. Nice features:
+ Deposits money
+ Withdraws money

##### Balance Sheet
Projection which downloads new events from Event Store and updates balance documents. Nice features:
+ Provides with balances of all the accounts
+ Checks event store for update per your request

### How to use it
Run app with Python 3 to perform example operations with accounts and print balances