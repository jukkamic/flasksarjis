import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ComicService } from '../comic.service';

@Component({
  selector: 'app-comic-list',
  templateUrl: './comic-list.component.html',
  styleUrls: ['./comic-list.component.css']
})
export class ComicListComponent implements OnInit {

  all_comics: any = [];
  comics: [{ name: any; display_name: any; index: any }] = [{ "name": "", "display_name": "", "index": 0 }];
  errors: any = [];

  constructor(private service: ComicService) {
    var i: number = -1;
    service.getAllNames().subscribe(
      (data: any) => {
        this.comics = data.List.map(
          (comic: { name: any; displayName: any; }) => {
            i++;
            return JSON.parse('{"name":"' + comic.name + '", "display_name":"' + comic.displayName + '", "index":' + i + '}');
          }
        )
      }
    );
    // this.comics.push({ "name": "fingerpori", display_name: "Fingerpori", index: 0 });
    // this.comics.push({ "name": "vw", display_name: "Viivi ja Wagner", index: 1 });
    // this.comics.push({ "name": "dilbert", display_name: "Dilbert", index: 2 });
    // this.comics.push({ "name": "luonto", display_name: "Kamala luonto", index: 3 });
    // this.comics.push({ "name": "xkcd", display_name: "Xkcd", index: 4 });
    // this.comics.push({ "name": "smbc", display_name: "SMBC", index: 5 });
    // this.comics.push({ "name": "fokit", display_name: "Fok_It", index: 6 });
    // this.comics.push({ "name": "redmeat", display_name: "Red Meat", index: 7 });
    // this.comics.push({ "name": "pbf", display_name: "Perry Bible Fellowship", index: 8 });
    // this.comics.push({"name": "velho", display_name: "Velho", index:9});
  }

  ngOnInit(): void {
    this.getAllInOrder();
  }

  private getAllInOrder() {
    var i;
    for (i in this.comics) {
      this.getOne(this.comics[i].name, this.comics[i].display_name, i);
    }
  }

  private getOne(name: string, display_name: string, index: any) {
    this.service.getLatestComic(name).subscribe(
      data => {
        this.all_comics[index] = data;
      },
      err => {
        this.all_comics[index] = null;
        this.errors.push("Error loading " + display_name);
      });
  }

}
