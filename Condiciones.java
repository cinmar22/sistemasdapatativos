public class Condiciones
{
  private int tamano;
  private double cantidadVelocidad;
  private boolean cieloDespejado;
  
  public Condiciones(int tamanoInicial)
  {
    actualizaCondiciones(tamanoInicial);
  }
  
  //Metodo para generar un numero aleatorio dentro de un rango
  public int generaNumAleatorio(int limInf,int limSup)
  {
	  double valor;
	  Double resultado;
	  
	  valor=Math.floor(Math.random()*(limSup-limInf+1)) + limInf;
	  
	  resultado=new Double(valor);
	  
	  return resultado.intValue();
  }
  
  public void actualizaCondiciones(int tamano)
  {
	 int aleatorio;
	  
    this.tamano=generaNumAleatorio(1,100);;
	
	if(tamano>=1  && tamano<=25) //0-2, 25-34                               tamano>= 0 && tamano <=25
	  cantidadVelocidad=generaNumAleatorio(1,100);
	  
	else if(tamano>26  && tamano<=35) //3-6, 21-24
		cantidadVelocidad=generaNumAleatorio(1,100);
		
	else if(tamano>=36  && tamano<=50) //7-10, 18-20
		cantidadVelocidad=generaNumAleatorio(1,100);
		
	
	aleatorio=generaNumAleatorio(0,1);
	
	if(aleatorio==0)
		cieloDespejado=false;
	else
		cieloDespejado=true;
  }
  
  public boolean getCieloDespejado()
  {
	  return cieloDespejado;
  }
  
  public int getTamano()
  {
	  return tamano;
  }
  
  public double getPorcentajeVelocidad()
  {
	  return cantidadVelocidad;
	  
  }
}