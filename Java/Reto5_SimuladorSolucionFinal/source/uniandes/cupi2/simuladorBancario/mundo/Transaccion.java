package uniandes.cupi2.simuladorBancario.mundo;

public class Transaccion {
	
	public enum Tipo{
		//Representa a apertura
		ENTRADA,
		//Representa el retiro.
		SALIDA
	}
	
	public enum Cuenta{
		
		AHORROS,
		
		CORRIENTE,
		
		CDT
	}
	
	private int consecutivo;
	private double valor;
	private Tipo tipo;
	private Cuenta cuenta;
	
	public Transaccion (int Tconsecutivo, double Tvalor, Tipo Ttipo, Cuenta Tcuenta){
		
		consecutivo = Tconsecutivo;
		valor= Tvalor;
		tipo = Ttipo;
		cuenta = Tcuenta;
	}
	
	public int darConsecutivo(){
		return consecutivo;
	}
	
	public double darValor(){
		return valor;
	}
	
	public int darTipoTransaccion(){
		return tipo.ordinal();
	}
	
	public int darCuentaTransaccion(){
		return cuenta.ordinal();
	}
	
	public Tipo darTipo(){
		return tipo;
	}
	
	public Cuenta darCuenta(){
		return cuenta;
	}
	
	
	

}
