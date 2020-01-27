import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { HttpService } from './http.service';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PetsComponent } from './pets/pets.component';
import { IndexComponent } from './pets/index/index.component';
import { NewComponent } from './pets/new/new.component';
import { ShowComponent } from './pets/show/show.component';
import { EditComponent } from './pets/edit/edit.component';

@NgModule({
  declarations: [
    AppComponent,
    PetsComponent,
    IndexComponent,
    NewComponent,
    ShowComponent,
    EditComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
