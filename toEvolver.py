"""
fnm = 'st2.fe';
fid = fopen(fnm,'wt');
fprintf(fid,'%6s\n','STRING');
fprintf(fid,'%17s\n\n','SPACE_DIMENSION 2');
fprintf(fid,'%45s\n\n','quantity len energy method edge_length global');
fprintf(fid,'%8s\n','VERTICES');
for k=1:length(pts)
 fprintf(fid,'%d %3.3f %3.3f %s\n',k,real(pts(k)),imag(pts(k)),'fixed');
end
fprintf(fid,'\n');

fprintf(fid,'%5s\n','EDGES');
for k=1:length(pts)-1
 fprintf(fid,'%d %d %d\n',k,edge(k,1),edge(k,2));
end
"""

def toevolver(pontosDir, arestasDir, filename):
    with open("pontos/cruzamento1.txt") as ptsFile:
        pontos = ptsFile.read()
    with open("arestas/arestas1.txt") as arestasFile:
        arestas = arestasFile.read()





toevolver([1,2,3])