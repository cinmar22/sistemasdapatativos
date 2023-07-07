public class SimuladorAutoAjuste
{
  public static void main(String args[])
  {
	  
	System.out.println();
    System.out.println("=== INICIANDO SIMULADOR DE Dificultad del Snake ===");
	System.out.println();
	System.out.println();
	
	HiloPercepcion percepcion=new HiloPercepcion();
	percepcion.start();
	HiloAccion accion=new HiloAccion(percepcion);
	accion.start();
	
  }
}