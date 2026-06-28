from app.graph.workflow import build_diligence_graph


def test_diligence_graph_completes():
    graph = build_diligence_graph()
    result = graph.invoke({
        "deal_name": "Acme Corp",
        "status": "pending",
        "messages": [],
    })

    assert result["status"] == "completed"
    assert result["deal_name"] == "Acme Corp"
    assert len(result["messages"]) == 3
    assert "Acme Corp" in result["messages"][0]
    assert "completed" in result["messages"][2].lower()
