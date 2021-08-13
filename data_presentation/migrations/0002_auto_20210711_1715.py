# Generated by Django 3.1.2 on 2021-07-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_presentation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funds2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_symbol', models.TextField(blank=True, null=True)),
                ('fund_extended_name', models.TextField(blank=True, null=True)),
                ('fund_family', models.TextField(blank=True, null=True)),
                ('inception_date', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('rating', models.TextField(blank=True, null=True)),
                ('return_rating', models.TextField(blank=True, null=True)),
                ('risk_rating', models.TextField(blank=True, null=True)),
                ('investment_strategy', models.TextField(blank=True, null=True)),
                ('investment_type', models.TextField(blank=True, null=True)),
                ('size_type', models.TextField(blank=True, null=True)),
                ('currency', models.TextField(blank=True, null=True)),
                ('fund_net_annual_expense_ratio', models.TextField(blank=True, null=True)),
                ('category_net_annual_expense_ratio', models.TextField(blank=True, null=True)),
                ('asset_cash', models.TextField(blank=True, null=True)),
                ('asset_stocks', models.TextField(blank=True, null=True)),
                ('asset_bonds', models.TextField(blank=True, null=True)),
                ('asset_others', models.TextField(blank=True, null=True)),
                ('asset_preferred', models.TextField(blank=True, null=True)),
                ('asset_convertable', models.TextField(blank=True, null=True)),
                ('price_earnings_ratio', models.TextField(blank=True, null=True)),
                ('price_book_ratio', models.TextField(blank=True, null=True)),
                ('price_sales_ratio', models.TextField(blank=True, null=True)),
                ('price_cashflow_ratio', models.TextField(blank=True, null=True)),
                ('median_market_cap', models.TextField(blank=True, null=True)),
                ('sector_basic_materials', models.TextField(blank=True, null=True)),
                ('sector_consumer_cyclical', models.TextField(blank=True, null=True)),
                ('sector_financial_services', models.TextField(blank=True, null=True)),
                ('sector_real_estate', models.TextField(blank=True, null=True)),
                ('sector_consumer_defensive', models.TextField(blank=True, null=True)),
                ('sector_healthcare', models.TextField(blank=True, null=True)),
                ('sector_utilities', models.TextField(blank=True, null=True)),
                ('sector_communication_services', models.TextField(blank=True, null=True)),
                ('sector_energy', models.TextField(blank=True, null=True)),
                ('sector_industrials', models.TextField(blank=True, null=True)),
                ('sector_technology', models.TextField(blank=True, null=True)),
                ('bond_maturity', models.TextField(blank=True, null=True)),
                ('bond_duration', models.TextField(blank=True, null=True)),
                ('credit_us_government', models.TextField(blank=True, null=True)),
                ('credit_aaa', models.TextField(blank=True, null=True)),
                ('credit_aa', models.TextField(blank=True, null=True)),
                ('credit_a', models.TextField(blank=True, null=True)),
                ('credit_bbb', models.TextField(blank=True, null=True)),
                ('credit_bb', models.TextField(blank=True, null=True)),
                ('credit_b', models.TextField(blank=True, null=True)),
                ('credit_below_b', models.TextField(blank=True, null=True)),
                ('credit_other_ratings', models.TextField(blank=True, null=True)),
                ('net_asset_value', models.TextField(blank=True, null=True)),
                ('fund_yield', models.TextField(blank=True, null=True)),
                ('top10_holdings', models.TextField(blank=True, null=True)),
                ('fund_return_ytd', models.TextField(blank=True, null=True)),
                ('category_return_ytd', models.TextField(blank=True, null=True)),
                ('fund_return_1month', models.TextField(blank=True, null=True)),
                ('category_return_1month', models.TextField(blank=True, null=True)),
                ('fund_return_3months', models.TextField(blank=True, null=True)),
                ('category_return_3months', models.TextField(blank=True, null=True)),
                ('fund_return_1year', models.TextField(blank=True, null=True)),
                ('category_return_1year', models.TextField(blank=True, null=True)),
                ('fund_return_3years', models.TextField(blank=True, null=True)),
                ('category_return_3years', models.TextField(blank=True, null=True)),
                ('fund_return_5years', models.TextField(blank=True, null=True)),
                ('category_return_5years', models.TextField(blank=True, null=True)),
                ('fund_return_10years', models.TextField(blank=True, null=True)),
                ('category_return_10years', models.TextField(blank=True, null=True)),
                ('fund_return_2019', models.TextField(blank=True, null=True)),
                ('category_return_2019', models.TextField(blank=True, null=True)),
                ('fund_return_2018', models.TextField(blank=True, null=True)),
                ('category_return_2018', models.TextField(blank=True, null=True)),
                ('fund_return_2017', models.TextField(blank=True, null=True)),
                ('category_return_2017', models.TextField(blank=True, null=True)),
                ('fund_return_2016', models.TextField(blank=True, null=True)),
                ('category_return_2016', models.TextField(blank=True, null=True)),
                ('fund_return_2015', models.TextField(blank=True, null=True)),
                ('category_return_2015', models.TextField(blank=True, null=True)),
                ('fund_return_2014', models.TextField(blank=True, null=True)),
                ('category_return_2014', models.TextField(blank=True, null=True)),
                ('fund_return_2013', models.TextField(blank=True, null=True)),
                ('category_return_2013', models.TextField(blank=True, null=True)),
                ('fund_return_2012', models.TextField(blank=True, null=True)),
                ('category_return_2012', models.TextField(blank=True, null=True)),
                ('fund_return_2011', models.TextField(blank=True, null=True)),
                ('category_return_2011', models.TextField(blank=True, null=True)),
                ('fund_return_2010', models.TextField(blank=True, null=True)),
                ('category_return_2010', models.TextField(blank=True, null=True)),
                ('years_up', models.TextField(blank=True, null=True)),
                ('years_down', models.TextField(blank=True, null=True)),
                ('fund_return_2020_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2020_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2020_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2019_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2019_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2019_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2019_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2018_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2018_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2018_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2018_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2017_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2017_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2017_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2017_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2016_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2016_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2016_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2016_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2015_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2015_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2015_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2015_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2014_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2014_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2014_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2014_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2013_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2013_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2013_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2013_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2012_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2012_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2012_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2012_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2011_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2011_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2011_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2011_q1', models.TextField(blank=True, null=True)),
                ('fund_return_2010_q4', models.TextField(blank=True, null=True)),
                ('fund_return_2010_q3', models.TextField(blank=True, null=True)),
                ('fund_return_2010_q2', models.TextField(blank=True, null=True)),
                ('fund_return_2010_q1', models.TextField(blank=True, null=True)),
                ('quarters_up', models.TextField(blank=True, null=True)),
                ('quarters_down', models.TextField(blank=True, null=True)),
                ('fund_alpha_3years', models.TextField(blank=True, null=True)),
                ('category_alpha_3years', models.TextField(blank=True, null=True)),
                ('fund_alpha_5years', models.TextField(blank=True, null=True)),
                ('category_alpha_5years', models.TextField(blank=True, null=True)),
                ('fund_alpha_10years', models.TextField(blank=True, null=True)),
                ('category_alpha_10years', models.TextField(blank=True, null=True)),
                ('fund_beta_3years', models.TextField(blank=True, null=True)),
                ('category_beta_3years', models.TextField(blank=True, null=True)),
                ('fund_beta_5years', models.TextField(blank=True, null=True)),
                ('category_beta_5years', models.TextField(blank=True, null=True)),
                ('fund_beta_10years', models.TextField(blank=True, null=True)),
                ('category_beta_10years', models.TextField(blank=True, null=True)),
                ('fund_mean_annual_return_3years', models.TextField(blank=True, null=True)),
                ('category_mean_annual_return_3years', models.TextField(blank=True, null=True)),
                ('fund_mean_annual_return_5years', models.TextField(blank=True, null=True)),
                ('category_mean_annual_return_5years', models.TextField(blank=True, null=True)),
                ('fund_mean_annual_return_10years', models.TextField(blank=True, null=True)),
                ('category_mean_annual_return_10years', models.TextField(blank=True, null=True)),
                ('fund_r_squared_3years', models.TextField(blank=True, null=True)),
                ('category_r_squared_3years', models.TextField(blank=True, null=True)),
                ('fund_r_squared_5years', models.TextField(blank=True, null=True)),
                ('category_r_squared_5years', models.TextField(blank=True, null=True)),
                ('fund_r_squared_10years', models.TextField(blank=True, null=True)),
                ('category_r_squared_10years', models.TextField(blank=True, null=True)),
                ('fund_standard_deviation_3years', models.TextField(blank=True, null=True)),
                ('category_standard_deviation_3years', models.TextField(blank=True, null=True)),
                ('fund_standard_deviation_5years', models.TextField(blank=True, null=True)),
                ('category_standard_deviation_5years', models.TextField(blank=True, null=True)),
                ('fund_standard_deviation_10years', models.TextField(blank=True, null=True)),
                ('category_standard_deviation_10years', models.TextField(blank=True, null=True)),
                ('fund_sharpe_ratio_3years', models.TextField(blank=True, null=True)),
                ('category_sharpe_ratio_3years', models.TextField(blank=True, null=True)),
                ('fund_sharpe_ratio_5years', models.TextField(blank=True, null=True)),
                ('category_sharpe_ratio_5years', models.TextField(blank=True, null=True)),
                ('fund_sharpe_ratio_10years', models.TextField(blank=True, null=True)),
                ('category_sharpe_ratio_10years', models.TextField(blank=True, null=True)),
                ('fund_treynor_ratio_3years', models.TextField(blank=True, null=True)),
                ('category_treynor_ratio_3years', models.TextField(blank=True, null=True)),
                ('fund_treynor_ratio_5years', models.TextField(blank=True, null=True)),
                ('category_treynor_ratio_5years', models.TextField(blank=True, null=True)),
                ('fund_treynor_ratio_10years', models.TextField(blank=True, null=True)),
                ('category_treynor_ratio_10years', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Funds',
        ),
    ]
