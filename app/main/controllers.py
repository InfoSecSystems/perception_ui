from . import main
from .models import InventoryHost
from flask import render_template, redirect, url_for
from flask.ext.login import login_required


@main.route('/')
@login_required
def root():
  return redirect(url_for('dashboards.overview'))

@main.route('/overview')
@login_required
def overview():
  return render_template('overview.html')

@main.route('/assets')
@login_required
def assets():
  inventory_hosts = InventoryHost.query.all()
  return render_template('assets.html', inventory_hosts=inventory_hosts)
