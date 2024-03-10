<?php

namespace Tests\Feature\Http\Controllers;

use App\Models\Author;
use App\Models\Link;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use JMac\Testing\Traits\AdditionalAssertions;
use PHPUnit\Framework\Attributes\Test;
use Tests\TestCase;

/**
 * @see \App\Http\Controllers\AuthorController
 */
final class AuthorControllerTest extends TestCase
{
    use AdditionalAssertions, RefreshDatabase, WithFaker;

    #[Test]
    public function index_behaves_as_expected(): void
    {
        $authors = Author::factory()->count(3)->create();

        $response = $this->get(route('author.index'));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function store_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\AuthorController::class,
            'store',
            \App\Http\Requests\AuthorStoreRequest::class
        );
    }

    #[Test]
    public function store_saves(): void
    {
        $name = $this->faker->name();
        $institution = $this->faker->word();
        $link = Link::factory()->create();

        $response = $this->post(route('author.store'), [
            'name' => $name,
            'institution' => $institution,
            'link_id' => $link->id,
        ]);

        $authors = Author::query()
            ->where('name', $name)
            ->where('institution', $institution)
            ->where('link_id', $link->id)
            ->get();
        $this->assertCount(1, $authors);
        $author = $authors->first();

        $response->assertCreated();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function show_behaves_as_expected(): void
    {
        $author = Author::factory()->create();

        $response = $this->get(route('author.show', $author));

        $response->assertOk();
        $response->assertJsonStructure([]);
    }


    #[Test]
    public function update_uses_form_request_validation(): void
    {
        $this->assertActionUsesFormRequest(
            \App\Http\Controllers\AuthorController::class,
            'update',
            \App\Http\Requests\AuthorUpdateRequest::class
        );
    }

    #[Test]
    public function update_behaves_as_expected(): void
    {
        $author = Author::factory()->create();
        $name = $this->faker->name();
        $institution = $this->faker->word();
        $link = Link::factory()->create();

        $response = $this->put(route('author.update', $author), [
            'name' => $name,
            'institution' => $institution,
            'link_id' => $link->id,
        ]);

        $author->refresh();

        $response->assertOk();
        $response->assertJsonStructure([]);

        $this->assertEquals($name, $author->name);
        $this->assertEquals($institution, $author->institution);
        $this->assertEquals($link->id, $author->link_id);
    }


    #[Test]
    public function destroy_deletes_and_responds_with(): void
    {
        $author = Author::factory()->create();

        $response = $this->delete(route('author.destroy', $author));

        $response->assertNoContent();

        $this->assertModelMissing($author);
    }
}
