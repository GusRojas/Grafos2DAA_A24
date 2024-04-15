from grafos2daa import *

grafo_malla = grafoMalla(25, 20)
grafo_malla.guardar_grafo("grafo_malla500.gv")
grafo_malla.generar_arbol_bfs_gv( "0-0", "arbol_bfs_malla500.gv")
grafo_malla.generar_arbol_dfsr_gv("1-0", "arbol_dfsr_malla500.gv")
grafo_malla.generar_arbol_dfsi_gv("0-1", "arbol_dfsi_malla500.gv")

grafo_erdos = grafoErdosRenyi(500,600)
grafo_erdos.guardar_grafo("grafo_erdos500.gv")
grafo_erdos.generar_arbol_bfs_gv( 1, "arbol_bfs_erdos500.gv")
grafo_erdos.generar_arbol_dfsr_gv(2, "arbol_dfsr_erdos500.gv")
grafo_erdos.generar_arbol_dfsi_gv(1, "arbol_dfsi_erdos500.gv")

grafo_gilbert = grafoGilbert(500,0.005)
grafo_gilbert.guardar_grafo("grafo_gilbert500.gv")
grafo_gilbert.generar_arbol_bfs_gv(1, "arbol_bfs_gilbert500.gv")
grafo_gilbert.generar_arbol_dfsr_gv(2, "arbol_dfsr_gilbert500.gv")
grafo_gilbert.generar_arbol_dfsi_gv(1, "arbol_dfsi_gilbert500.gv")

grafo_geo = grafoGeografico(500,0.005)
grafo_geo.guardar_grafo("grafo_geo500.gv")
grafo_geo.generar_arbol_bfs_gv( 1, "arbol_bfs_geo500.gv")
grafo_geo.generar_arbol_dfsr_gv(2, "arbol_dfsr_geo500.gv")
grafo_geo.generar_arbol_dfsi_gv(1, "arbol_dfsi_geo500.gv")

grafo_barabasi = grafoBarabasiAlbert(500,2)
grafo_barabasi.guardar_grafo("grafo_barabasi500.gv")
grafo_barabasi.generar_arbol_bfs_gv( 1, "arbol_bfs_barabasi500.gv")
grafo_barabasi.generar_arbol_dfsr_gv(2, "arbol_dfsr_barabasi500.gv")
grafo_barabasi.generar_arbol_dfsi_gv(1, "arbol_dfsi_barabasi500.gv")

grafo_dorogov = grafoDorogovtsevMendes(500)
grafo_dorogov.guardar_grafo("grafo_dorogov500.gv")
grafo_dorogov.generar_arbol_bfs_gv(1, "arbol_bfs_dorogov500.gv")
grafo_dorogov.generar_arbol_dfsr_gv( 8, "arbol_dfsr_dorogov500.gv")
grafo_dorogov.generar_arbol_dfsi_gv( 1, "arbol_dfsi_dorogov500.gv")