/* Esta clase lo que va a hacer es generar percepciones (datos) cada cierto tiempo. */

public class HiloPercepcion extends Thread
{
	private Condiciones c;
	private int tamano;
	
	
  /* Constructor */
  public HiloPercepcion()
  {
	  tamano=0;
	  c=new Condiciones(tamano);
  }
   
   public Condiciones getCondiciones()
   {
	   return c;
   }
   
  /* Metodo que deben implementar todos los hilos */
  public void run()
  {
	  
    try{
	  /* Ciclo infinito */
	  while(true)
	  {
		  
		tamano=5+tamano;
		c.actualizaCondiciones(tamano%30);
	    sleep(30);
	  }
	}catch(InterruptedException e){
	  System.out.println(e.getMessage());
	}
  }
}