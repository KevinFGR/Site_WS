using Microsoft.AspNetCore.Mvc;
using Torgon.API.Models;
using Torgon.API.Repositorios.Interfaces;

namespace Torgon.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ClientController : ControllerBase
{
    private readonly IClientRepositorio _clientRepositorio;
    public ClientController(IClientRepositorio clientRepositorio)
    {
        _clientRepositorio = clientRepositorio;
    }
    [HttpGet]
    public async Task<ActionResult<ClientModel[]>> GetAllClients(){
        List<ClientModel> clients = await _clientRepositorio.GetAllClients();
        return Ok(clients);
    }
    [HttpGet("{id}")]
    public async Task<ActionResult<ClientModel>> GetClientById(int id){
        ClientModel client = await _clientRepositorio.GetClientById(id);
        return Ok(client);
    }
    [HttpPost]
    public async Task<ActionResult<ClientModel>> AddClient(ClientModel model){
        await _clientRepositorio.AddClient(model);
        return Ok(model);
    }

    [HttpPut]
    public async Task<ActionResult<ClientModel>> UpdateClient(ClientModel model, int id){
        ClientModel client = await _clientRepositorio.GetClientById(id);
        if(client == null){
            throw new Exception("Client by id {id} not found");
        }
        model.Id = client.Id;
        ClientModel newClient = await _clientRepositorio.UpdateClient(model, id);
        
        return Ok(newClient);
    }
    [HttpDelete]
    public async Task<ActionResult<bool>> DeleteClient(int id){
        ClientModel client = await _clientRepositorio.GetClientById(id);
        if(client == null){
            throw new Exception("Client by id {id} not found");
        }
        bool deleted = await _clientRepositorio.DeleteClient(id);
        return Ok(deleted);
    }
}
