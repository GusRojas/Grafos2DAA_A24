from grafos2daa import *

grafo_malla = grafoMalla(5, 6)
grafo_malla.guardar_grafo("grafo_malla30.gv")
grafo_malla.generar_arbol_bfs_gv( "0-0", "arbol_bfs_malla30.gv")

grafo_erdos = grafoErdosRenyi(30,100)
grafo_erdos.guardar_grafo("grafo_erdos30.gv")
grafo_erdos.generar_arbol_bfs_gv( 1, "arbol_bfs_erdos30.gv")

grafo_gilbert = grafoGilbert(30,0.20)
grafo_gilbert.guardar_grafo("grafo_gilbert30.gv")
grafo_gilbert.generar_arbol_bfs_gv(1, "arbol_bfs_gilbert30.gv")

grafo_geo = grafoGeografico(30,0.10)
grafo_geo.guardar_grafo("grafo_geo30.gv")
grafo_geo.generar_arbol_bfs_gv( 1, "arbol_bfs_geo30.gv")

grafo_barabasi = grafoBarabasiAlbert(30,2)
grafo_barabasi.guardar_grafo("grafo_barabasi30.gv")
grafo_barabasi.generar_arbol_bfs_gv( 1, "arbol_bfs_barabasi30.gv")

grafo_dorogov = grafoDorogovtsevMendes(30)
grafo_dorogov.guardar_grafo("grafo_dorogov30.gv")
grafo_dorogov.generar_arbol_bfs_gv(1, "arbol_bfs_dorogov30.gv")
grafo_dorogov.generar_arbol_dfsr_gv( 8, "arbol_dfsr_dorogov30.gv")
grafo_dorogov.generar_arbol_dfsi_gv( 1, "arbol_dfsi_dorogov30.gv")