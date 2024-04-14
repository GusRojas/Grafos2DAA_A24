from grafos2daa import *

grafo_malla = grafoMalla(10, 10)
grafo_malla.guardar_grafo("grafo_malla100.gv")
grafo_malla.generar_arbol_bfs_gv( "0-0", "arbol_bfs_malla100.gv")
grafo_malla.generar_arbol_dfsr_gv("1-0", "arbol_dfsr_malla100.gv")
grafo_malla.generar_arbol_dfsi_gv("0-1", "arbol_dfsi_malla100.gv")

grafo_erdos = grafoErdosRenyi(100,350)
grafo_erdos.guardar_grafo("grafo_erdos100.gv")
grafo_erdos.generar_arbol_bfs_gv( 1, "arbol_bfs_erdos100.gv")
grafo_erdos.generar_arbol_dfsr_gv(2, "arbol_dfsr_erdos100.gv")
grafo_erdos.generar_arbol_dfsi_gv(1, "arbol_dfsi_erdos100.gv")

grafo_gilbert = grafoGilbert(100,0.20)
grafo_gilbert.guardar_grafo("grafo_gilbert100.gv")
grafo_gilbert.generar_arbol_bfs_gv(1, "arbol_bfs_gilbert100.gv")
grafo_gilbert.generar_arbol_dfsr_gv(2, "arbol_dfsr_gilbert100.gv")
grafo_gilbert.generar_arbol_dfsi_gv(1, "arbol_dfsi_gilbert100.gv")


grafo_geo = grafoGeografico(100,0.10)
grafo_geo.guardar_grafo("grafo_geo100.gv")
grafo_geo.generar_arbol_bfs_gv( 1, "arbol_bfs_geo100.gv")
grafo_geo.generar_arbol_dfsr_gv(2, "arbol_dfsr_geo100.gv")
grafo_geo.generar_arbol_dfsi_gv(1, "arbol_dfsi_geo100.gv")

grafo_barabasi = grafoBarabasiAlbert(100,2)
grafo_barabasi.guardar_grafo("grafo_barabasi100.gv")
grafo_barabasi.generar_arbol_bfs_gv( 1, "arbol_bfs_barabasi100.gv")
grafo_barabasi.generar_arbol_dfsr_gv(2, "arbol_dfsr_barabasi100.gv")
grafo_barabasi.generar_arbol_dfsi_gv(1, "arbol_dfsi_barabasi100.gv")

grafo_dorogov = grafoDorogovtsevMendes(100)
grafo_dorogov.guardar_grafo("grafo_dorogov100.gv")
grafo_dorogov.generar_arbol_bfs_gv(1, "arbol_bfs_dorogov100.gv")
grafo_dorogov.generar_arbol_dfsr_gv( 8, "arbol_dfsr_dorogov100.gv")
grafo_dorogov.generar_arbol_dfsi_gv( 1, "arbol_dfsi_dorogov100.gv")