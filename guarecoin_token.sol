// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GUARECOIN {
    string public constant name = "GUARECOIN";
    string public constant symbol = "GRC";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Coordenada sagrada del manifiesto
    string public constant MANIFIESTO_HASH = "0xTU_HASH_DE_TRANSACCION"; // ← reemplaza con el hash real

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Saldo insuficiente");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[_from] >= _value, "Saldo insuficiente");
        require(allowance[_from][msg.sender] >= _value, "No autorizado");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // 🔐 Valor soberano con piso de 0.98 USD
    function calcularValor(uint256 totalComprasUSDT, uint256 enCirculacion) public pure returns (uint256 valorGUARECOIN) {
        require(enCirculacion > 0, "Circulación inválida");
        uint256 calculado = totalComprasUSDT * 1e18 / enCirculacion;
        uint256 piso = 98 * 1e16; // 0.98 en formato 18 decimales
        return calculado >= piso ? calculado : piso;
    }
}