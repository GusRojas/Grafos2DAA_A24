from grafos2daa import *

grafo_malla = grafoMalla(25, 20)
grafo_malla.guardar_grafo("grafo_malla500.gv")
grafo_malla.generar_arbol_bfs_gv( "0-0", "arbol_bfs_malla500.gv")

grafo_erdos = grafoErdosRenyi(500,1800)
grafo_erdos.guardar_grafo("grafo_erdos500.gv")
grafo_erdos.generar_arbol_bfs_gv( 1, "arbol_bfs_erdos500.gv")

grafo_gilbert = grafoGilbert(500,0.20)
grafo_gilbert.guardar_grafo("grafo_gilbert500.gv")
grafo_gilbert.generar_arbol_bfs_gv(1, "arbol_bfs_gilbert500.gv")

grafo_geo = grafoGeografico(500,0.10)
grafo_geo.guardar_grafo("grafo_geo500.gv")
grafo_geo.generar_arbol_bfs_gv( 1, "arbol_bfs_geo500.gv")

grafo_barabasi = grafoBarabasiAlbert(500,2)
grafo_barabasi.guardar_grafo("grafo_barabasi500.gv")
grafo_barabasi.generar_arbol_bfs_gv( 1, "arbol_bfs_barabasi500.gv")

grafo_dorogov = grafoDorogovtsevMendes(500)
grafo_dorogov.guardar_grafo("grafo_dorogov500.gv")
grafo_dorogov.generar_arbol_bfs_gv(1, "arbol_bfs_dorogov500.gv")
#grafo_dorogov.generar_arbol_dfsr_gv( 8, "arbol_dfsr_dorogov100.gv")
#grafo_dorogov.generar_arbol_dfsi_gv( 1, "arbol_dfsi_dorogov100.gv")