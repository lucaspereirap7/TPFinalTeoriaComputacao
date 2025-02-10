from typing import Union
from fastapi import FastAPI, HTTPException, Request
from automata.fa.dfa import DFA
from automata.pda.dpda import DPDA
from automata.tm.dtm import DTM

app = FastAPI()

# Deterministic Finite Automaton (DFA)
@app.post("/dfa")
async def dfa(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if not states or not input_symbols or not transitions or not initial_state or not final_states or input_w == "":
        raise HTTPException(status_code=400, detail="Invalid input")

    dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    return {"accepted": dfa.accepts_input(input_w), "input": input_w}


# Deterministic Pushdown Automaton (DPDA)
@app.post("/dpda")
async def dpda(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    stack_symbols = set(info.get("stack_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    initial_stack_symbol = info.get("initial_stack_symbol", "")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if not states or not input_symbols or not stack_symbols or not transitions or not initial_state or not initial_stack_symbol or not final_states or input_w == "":
        raise HTTPException(status_code=400, detail="Invalid input")

    dpda = DPDA(
        states=states,
        input_symbols=input_symbols,
        stack_symbols=stack_symbols,
        transitions=transitions,
        initial_state=initial_state,
        initial_stack_symbol=initial_stack_symbol,
        final_states=final_states,
        acceptance_mode="final_state"
    )

    return {"accepted": dpda.accepts_input(input_w), "input": input_w}


# Turing Machine (DTM)
@app.post("/tm")
async def tm(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    tape_symbols = set(info.get("tape_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    blank_symbol = info.get("blank_symbol", "_")
    final_states = set(info.get("final_states", []))
    input_w = info.get("input_w", "")

    if not states or not input_symbols or not tape_symbols or not transitions or not initial_state or not final_states or input_w == "":
        raise HTTPException(status_code=400, detail="Invalid input")

    dtm = DTM(
        states=states,
        input_symbols=input_symbols,
        tape_symbols=tape_symbols,
        transitions=transitions,
        initial_state=initial_state,
        blank_symbol=blank_symbol,
        final_states=final_states
    )

    return {"accepted": dtm.accepts_input(input_w), "input": input_w}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Automata API"}
