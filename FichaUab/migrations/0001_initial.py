# Generated by Django 4.1.7 on 2023-03-23 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_de_curso', models.CharField(choices=[('Graduação (Bacharelado)', 'Graduação (Bacharelado)'), ('Graduação (Licenciatura)', 'Graduação (Licenciatura)'), ('Extensão', 'Extensão'), ('Especialização', 'Especialização'), ('Aperfeiçoamanto', 'Aperfeiçoamento'), ('Tecnólogo', 'Tecnólogo')], max_length=127)),
                ('email_curso', models.EmailField(max_length=254)),
                ('telefone_curso', models.CharField(max_length=15)),
                ('ativo', models.BooleanField()),
                ('descricao', models.TextField()),
                ('perfil_egresso', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=31)),
                ('bairro', models.CharField(max_length=127)),
                ('cidade', models.CharField(max_length=127)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Polo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email_institucional', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('ativo', models.BooleanField()),
                ('classificacao_seed', models.CharField(choices=[('L', 'L - Polo com interrupção de entrada de estudantes nos cursos que necessitam de laboratório'), ('R', 'R - Polo com interrupção de entrada de estudantes'), ('S', 'S - Polo com infraestrutura suficiente'), ('T', 'T - Polo com recomendação de melhoria')], max_length=1)),
                ('possui_biblioteca_municipal', models.BooleanField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('apresentacao', models.TextField()),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FichaUab.pessoa')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FichaUab.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('responsavel', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.CharField(choices=[('Municipal', 'Municipal'), ('Estadual', 'Estadual')], max_length=15)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FichaUab.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('carga_horaria', models.IntegerField()),
                ('tipo_disciplina', models.CharField(max_length=55)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FichaUab.curso')),
            ],
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=127)),
                ('agencia', models.CharField(max_length=31)),
                ('conta', models.CharField(max_length=31)),
                ('operacao', models.CharField(blank=True, max_length=7, null=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUab.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='coordenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='FichaUab.pessoa'),
        ),
    ]
