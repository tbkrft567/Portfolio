import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PetsComponent } from './pets/pets.component';
import { NewComponent } from './pets/new/new.component';
import { IndexComponent } from './pets/index/index.component';
import { EditComponent } from './pets/edit/edit.component';
import { ShowComponent } from './pets/show/show.component';


const routes: Routes = [
  { path: 'pets', redirectTo: 'pets/index', pathMatch: 'full'},
  { path: 'pets', component: PetsComponent, children: [
    {path: 'new', component: NewComponent },
    {path: 'index', component: IndexComponent },
    {path: ':petId/edit', component: EditComponent },
    {path: ':petId/show', component: ShowComponent },
  ]},

  { path: '', redirectTo: 'pets/index', pathMatch: 'full'},
  { path: '**', redirectTo: 'pets/index', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
