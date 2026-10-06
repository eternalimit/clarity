# Spider -> Monkey Bus -> Web/Net Hooks

## Canonical Script

SPIDER  
finds + traces + verifies  
↓  
TCGE GATE  
PASS or HOLD  
↓  
MONKEY BUS  
carries only PASS payload  
↓  
HOOK  
API / webhook / connector adapter  
↓  
WEB / NET  
external service  
↓  
RECEIPT  
response / event ID / status  
↓  
ECHO  
independent verification

## Hook Interface Contract

Each hook requires:

1. Input schema — what data can enter.
2. Authorization rule — what is allowed to leave the bus.
3. Destination binding — the exact endpoint allowed to receive it.
4. Receipt / Echo — evidence that the destination accepted it and an independent validation step.

## TCGE Rule

R = Reality  
I = Inference  
E = Echo  

K = R AND I AND E

If required evidence is unresolved: HOLD.

## Boundary

Spider may discover, trace, and verify.  
Monkey Bus may transport only payloads that passed the TCGE gate.  
Hooks are adapters, not authority.  
External acceptance is not knowledge until receipt and Echo are validated.

Signed: Richard Stein

Digest:
Spider -> TCGE Gate -> Monkey Bus -> Hook -> Web/Net -> Receipt -> Echo

Index Handoff:
SPIDER_MONKEY_BUS_WEB_NET_HOOKS
