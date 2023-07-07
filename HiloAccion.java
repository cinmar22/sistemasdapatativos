public class HiloAccion extends Thread
{
	private HiloPercepcion percepcion;
	private int velocidad12;
	private static final String[] velocidad2={"lenta", "Moderada","Rapida"};
	

	public HiloAccion(HiloPercepcion percepcion)
	{
      this.percepcion=percepcion;	 
	}
	
	public void realizaAjuste()
	{
	  int tamano;
	  double velocidad;
	  boolean despejado;
	  
	  Condiciones c=percepcion.getCondiciones();
	  tamano=c.getTamano();
	  velocidad=c.getPorcentajeVelocidad();
	  despejado=c.getCieloDespejado();
	  
	  /* Reglas para el ajuste */
	  if(velocidad>=1 &&velocidad<=50 && despejado )
	   velocidad12=0;
	   
	  else if(velocidad>= 51 && velocidad<=79 && despejado)
	   velocidad12=1;

	   else
	   velocidad12=2;
	   
	   despliegaStatus(tamano, velocidad, despejado);
	   
	  
	}
	
	public void despliegaStatus(int tamano, double velocidad, boolean despejado)
	{
		
		String tamano2;
		double dificultad;
		
		  
		  
		  
		  
		if(tamano>= 1 && tamano <=25)
			tamano2= "corto";
			else if(tamano >= 26 && tamano <=35)
			tamano2="mediano";
			else 
			tamano2="largo"; 
	// eso para la dificultad
if(tamano>= 1 && tamano <=25  && velocidad>=1 && velocidad<=79) 
			
	dificultad=15.2;
	else if(tamano>= 1 && tamano <=35 && velocidad>=1 && velocidad<=50 )
	dificultad=22.1;
	
 else if  (tamano>= 1 && tamano <=25 && velocidad>=80 && velocidad<=100 )
	
				dificultad=38.8;
	else if (tamano >= 26 && tamano <=35 && velocidad>= 51 && velocidad<=79)
			dificultad=60.4;
	else if(tamano>=36 && tamano<=100 && velocidad>=1 &&velocidad<=50)
		dificultad=72.1;
		
else if( tamano >= 26 && tamano <=35 && velocidad>=80 && velocidad<=100)
		dificultad=78.4;
		
else if ( tamano>=36 && tamano <=100 && velocidad>= 51 && velocidad<=100)

	dificultad=97;

	   else 
	   dificultad=00;
	   
	   System.out.println("CONDICIONES ACTUALES--El tamaño  tiene "+
	   String.valueOf(tamano) + " de longitud,  con una velocidad de "+ String.valueOf(velocidad) + "  y La dificultad esta en  " + dificultad );
	   
	   System.out.println();
	}
	
  public void run()
  {    
	
    try{
		while(true)
		{
			realizaAjuste();
			sleep(2000);
		}
	}catch(InterruptedException e){
	  System.out.println(e.getMessage());
	}
  }
}