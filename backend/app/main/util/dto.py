from flask_restx import Namespace, fields
from .. model.perfil import Perfil

class PerfilDto:
    api = Namespace('perfis', description='Operações com Perfis de Usuario')
    perfil = api.model('perfil', {
        'id' : fields.Integer(description = 'id do perfil'),
        'nome': fields.String(required=True, description='nome do perfil'),
        'uri' : fields.Url('api.perfis_perfil', readonly=True),
        'ativo': fields.Boolean(description='ativo'),
    })
    perfilinsert = api.model('perfilinsert', {
        'nome': fields.String(required=True, description='nome do perfil'),
    })
    perfilupdate = api.model('perfilupdate', {
        'nome': fields.String(required=True, description='nome do perfil'),
        'ativo': fields.Boolean(description='ativo'),
    })

class UsuarioDto:
    api = Namespace('usuarios', description='Operações com usuários')

    usuarioinsert = api.model('usuarioinsert', {
        'login': fields.String(required=True),
        'nome' : fields.String(required=True),
        'senha': fields.String(required=True),
        'perfil_id': fields.Integer(required=True, description='id do perfil')
    })
    usuariolist = api.model('usuariolist', {
        'id'  : fields.Integer(readonly=True),
        'login': fields.String(required=True),
        'nome' : fields.String(required=True),
        'ativo': fields.Boolean(),
        'uri' : fields.Url('api.usuarios_usuario_id'),
        'perfil_id': fields.Integer( description='id do perfil')
    })
    usuarioupdate = api.model('usuarioupdate', {
        'login': fields.String(required=False),
        'nome' : fields.String(required=False),
        'senha': fields.String(required=False),
        'perfil_id': fields.Integer(required=False, description='id do perfil'),
        'ativo': fields.Boolean(required=False,description='inativa/ativa usuário'),
    })

class ProdutoDto:    
    api = Namespace('produtos', description='Operações com Produtos')
    produtoinsert = api.model('produto', {
        'nome': fields.String(required=True, description='nome do produto'),
        'codigo_barra': fields.String(required=True,description='Código de barra do Produto'),  
        'preco_venda' : fields.Float(description='preco de venda do produto'),      
        'fornecedor_id' : fields.Integer(required=True, description='id do fornecedor'),        
    })
    produtolist = api.model('produtolist', {
        'id'  : fields.Integer(readonly=True),
        'nome': fields.String(required=True, description='nome do produto'),
        'codigo_barra': fields.String(description='Código de barra do Produto'),
        'uri' : fields.Url('api.produtos_produto_id'),
        'fornecedor_id' : fields.Integer( description='id do fornecedor'),
        'preco_venda' : fields.Float(description='preco de venda do produto'),
        'saldo' : fields.Float(description='quantidade do produto em estoque'),
        'ativo': fields.Boolean(required=False,description='inativa/ativa produto'),
    })
    produtoupdate = api.model('produtoupdate', {
        'nome': fields.String(required=False, description='nome do produto'),
        'codigo_barra': fields.String(required=False,description='Código de barra do Produto'),
        'fornecedor_id' : fields.Integer(required=False, description='id do fornecedor'),
        'uri' : fields.Url('api.produtos_produto_id', readonly=True),
        'preco_venda' : fields.Float(description='preco de venda do produto'),
        'ativo': fields.Boolean(required=False,description='inativa/ativa produto')        
    })
    produtoupdateretorno = api.model('produtoupdate', {
        'nome': fields.String(required=False, description='nome do produto'),
        'codigo_barra': fields.String(required=False,description='Código de barra do Produto'),
        'fornecedor_id' : fields.Integer(required=False, description='id do fornecedor'),
        'uri' : fields.Url('api.produtos_produto_id', readonly=True),
        'preco_venda' : fields.Float(description='preco de venda do produto'),
        'saldo' : fields.Float(description='quantidade do produto em estoque'),        
        'ativo': fields.Boolean(required=False,description='inativa/ativa produto'),
        'status': fields.String(required=False,description='status da execucao da operacao'),
        'message': fields.String(required=False,description='descricao do resultado da operacao'),
    })

class PrecoDto:
    api = Namespace('precos', description='Operações com Precos')
    precoinsert = api.model('preco', {
        'preco_venda': fields.Float(required=True, description='Preço de venda'),        
        'produto_id': fields.Integer(required=True, description='Id do produto'),
    })
    precolista = api.model('precolista', {
        'id'  : fields.Integer(readonly=True),
        'preco_venda': fields.Float(description='Preço de venda'),
        'data_emissao': fields.DateTime(description='Data da movimentação'),
        'usuario_id': fields.Integer(description='Id do usuario'),
        'produto_id': fields.Integer(description='Id do produto'),
        'ativo': fields.Boolean(description='inativa/ativa preço')
    })
    precoproduto = api.model('precoproduto', {
        'preco_venda': fields.Float(description='Preço de venda'),
        'data_emissao': fields.DateTime(description='Data da movimentação'),
    })

class MovimentacaoDto:
    api = Namespace('movimentacoes', description='Operações com Movimentacoes (tipo_movimentação "E"(Entrada) / "S" (Saida)')
    movimentacaoinsert = api.model('movimentacaoinsert', {
        'local_estoque': fields.String(required=True, description='Local de estoque'),
        'tipo_movimentacao': fields.String(required=True, description='Tipo movimentação a LETRA de E - Entrada ou S - Saida.'),
        'preco_total': fields.Float(required=True, description='Preço Total'),
        'quantidade': fields.Integer(required=True, description='Quantidade de produto.'),        
        'produto_id': fields.Integer(required=True, description='Id do produto'),
    })    
    movimentacao_lista = api.model('movimentacaolista', {
        'id'  : fields.Integer(readonly=True),
        'local_estoque': fields.String(description='Local de estoque'),
        'tipo_movimentacao': fields.String(description='Tipo movimentação a LETRA de E - Entrada ou S - Saida.'),
        'preco_total': fields.Float(description='Preço Total'),
        'quantidade': fields.Integer(description='Quantidade de produto.'),
        'usuario_id': fields.Integer(description='Id do usuario'),
        'produto_id': fields.Integer(description='Id do produto'),
        'data_movimentacao': fields.DateTime(),
        'ativo': fields.Boolean(description='inativa/ativa movimento'),
        'produto.nome':fields.String(description='Nome do produto'),
        'usuario.nome':fields.String(description='Nome do usuario'),
    })
    movimentacao_saldo = api.model('movimentacaosaldo', {
        'quantidade': fields.Integer(description='Quantidade que existe no estoque')
    })

class FornecedorDto:
    api = Namespace('fornecedores', description='Operações com Fornecedores')
    fornecedorinsert = api.model('fornecedor', {
        'cnpj': fields.String(required=True, description='cpnj do fornecedor'),
        'nome': fields.String(required=True, description='nome fornecedor'),
        'logradouro': fields.String(required=True, description='rua, avenida, estrada, etc'),
        'numero': fields.String(required=True, description='numero do endereço'),
        'complemento': fields.String(required=False, description='complemento do endereço'),
        'bairro': fields.String(required=True, description='bairro'),
        'cidade': fields.String(required=True, description='cidade'),
        'estado': fields.String(required=True, description='estado'),
        'cep': fields.String(required=True, description='cep'),
    })
    fornecedorlista = api.model('fornecedores', {
        'id': fields.String(description='id do fornecedor'),
        'cnpj': fields.String(description='cpnj do fornecedor'),
        'nome': fields.String(description='nome fornecedor'),
        'logradouro': fields.String(description='rua, avenida, estrada, etc'),
        'numero': fields.String(description='numero do endereço'),
        'complemento': fields.String(description='complemento do endereço'),
        'bairro': fields.String(description='bairro'),
        'cidade': fields.String(description='cidade'),
        'estado': fields.String(description='estado'),
        'cep': fields.String(description='cep'),
        'ativo': fields.Boolean(description='ativo'),
    })
    fornecedorupdate = api.model('fornecedorupdate', {
        'nome': fields.String(description='nome fornecedor'),
        'logradouro': fields.String(description='rua, avenida, estrada, etc'),
        'numero': fields.String(description='numero do endereço'),
        'complemento': fields.String(description='complemento do endereço'),
        'bairro': fields.String(description='bairro'),
        'cidade': fields.String(description='cidade'),
        'estado': fields.String(description='estado'),
        'cep': fields.String(description='cep'),
        'ativo': fields.Boolean(description='ativo'),
    })

class TipoContatoDto:
    api = Namespace('tipocontatos', description='Operações com Tipo Contato dos Contatos')
    tipocontatoinsert = api.model('tipocontato', {
        'nome': fields.String(required=True, description='nome do tipo contato'),
    })
    tipocontatolista = api.model('tipocontatos', {
        'id': fields.Integer(description='id do tipo contato'),
        'nome': fields.String(description='nome do tipo contato'),
        'ativo': fields.Boolean(description='status do tipo contato'),
    })
    tipocontatoupdate = api.model('tipocontatoupdate', {
        'nome': fields.String(description='nome do tipo contato'),
        'ativo': fields.Boolean(description='status do tipo contato'),
    })

class ContatoDto:
    api = Namespace('contatos', description='Operações com contatos')
    contatoinsert = api.model('contato', {
        'valor': fields.String(required=True, description='valor contato'),
        'tipocontato_id': fields.Integer(required=True, description='id do tipo contato'),
        'fornecedor_id': fields.Integer(required=True, description='id do fornecedor'),
    })
    contatolista = api.model('contatos', {
        'id': fields.String(description='id do contato'),
        'valor': fields.String(required=True, description='valor contato'),
        'tipocontato_id': fields.Integer(required=True, description='id do tipo contato'),
        'fornecedor_id': fields.Integer(required=True, description='id do fornecedor'),
        'ativo': fields.Boolean(description='status do contato'),
    })
    contatoupdate = api.model('contatoupdate', {
        'valor': fields.String(description='valor contato'),
        'tipocontato_id': fields.Integer(description='id do tipo contato'),
        'ativo': fields.Boolean(description='status do contato'),
    })



class AuthDto:
    api = Namespace('auth', description='Operações de autenticação')
    usuario_auth = api.model('auth_details', {
        'login': fields.String(required=True, description='login do usuário'),
        'senha': fields.String(required=True, description='senha do usuário'),
    })
    usuario_auth_reset_password = api.model('usuario_auth_reset_password', {
        'login': fields.String(required=True, description='login do usuário'),
        'novasenha': fields.String(required=True, description='nova senha do usuário'),
    })
    usuario_auth_change_password = api.model('usuario_auth_change_password', {
        'login': fields.String(required=True, description='login do usuário'),
        'senha': fields.String(required=True, description='senha do usuário'),
        'novasenha': fields.String(required=True, description='nova senha do usuário'),
    })
