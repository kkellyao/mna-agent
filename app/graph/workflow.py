from langgraph.graph import END, StateGraph

from app.graph.state import DiligenceState


def start_diligence(state: DiligenceState) -> dict:
    return {
        "status": "in_progress",
        "messages": [f"Starting diligence for {state['deal_name']}"],
    }


def analyze_placeholder(state: DiligenceState) -> dict:
    return {
        "status": "analyzing",
        "messages": ["Placeholder analysis complete. Awaiting real agent integration."],
    }


def complete_diligence(state: DiligenceState) -> dict:
    return {
        "status": "completed",
        "messages": [f"Diligence completed for {state['deal_name']}"],
    }


def build_diligence_graph():
    graph = StateGraph(DiligenceState)

    graph.add_node("start_diligence", start_diligence)
    graph.add_node("analyze_placeholder", analyze_placeholder)
    graph.add_node("complete_diligence", complete_diligence)

    graph.set_entry_point("start_diligence")
    graph.add_edge("start_diligence", "analyze_placeholder")
    graph.add_edge("analyze_placeholder", "complete_diligence")
    graph.add_edge("complete_diligence", END)

    return graph.compile()
