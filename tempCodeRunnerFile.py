node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_a, node_c) == True

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_d, node_e) == False

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_a, node_g) == True

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_g, node_b) == False