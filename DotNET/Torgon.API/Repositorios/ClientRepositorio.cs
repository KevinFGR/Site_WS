using Torgon.API.Repositorios.Interfaces;
using Torgon.API.Models;
using Microsoft.AspNetCore.Http.HttpResults;
using Torgon.API.Data;
using Microsoft.EntityFrameworkCore;
using System.Reflection.Metadata.Ecma335;

namespace Torgon.API.Repositorios;

public class ClientRepositorio : IClientRepositorio
{
    private readonly TorgonDBContext _context;
    public ClientRepositorio(TorgonDBContext context)
    {
        _context = context;
        _context.ChangeTracker.QueryTrackingBehavior = QueryTrackingBehavior.NoTracking;
    }
    public async Task<List<ClientModel>> GetAllClients()
    {
        return await _context.Clients.ToListAsync();
    }

    public async Task<ClientModel> GetClientById(int id)
    {
        return await _context.Clients.FirstOrDefaultAsync(x=>x.Id==id);
    }
    public async Task<ClientModel> AddClient(ClientModel model)
    {
        await _context.Clients.AddAsync(model);
        await _context.SaveChangesAsync();
        return model;
    }

    public async Task<ClientModel> UpdateClient(ClientModel model, int id)
    {
        ClientModel client = await GetClientById(id);

        model.Id = client.Id;
        _context.Clients.Update(model);
        await _context.SaveChangesAsync();

        return model; 
    }

    public async Task<bool> DeleteClient(int id)
    {
        ClientModel client = await GetClientById(id);
        _context.Clients.Remove(client);
        await _context.SaveChangesAsync();

        return true; 
    }

}